import streamlit as st
import cv2
from ultralytics import YOLO
import torch
import numpy as np
from sort.sort import Sort
from util import get_car, read_license_plate  

import torch

# Désactivez CUDA
torch.cuda.is_available = lambda: False

# Titre de l'application
st.title("Système de Reconnaissance de Plaques - YOLOv8")

# Section de téléchargement de la vidéo
st.subheader("Upload your video")
uploaded_file = st.file_uploader("Drag and drop or click to upload a video", type=["mp4"])

if uploaded_file is not None:
    # Sauvegarder la vidéo téléchargée temporairement
    input_path = "./uploaded_video.mp4"
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())
    
    st.success("Video uploaded successfully!")

    # Détecter les plaques et générer la sortie
    st.subheader("Processing the video...")

    try:
        # Vérification du GPU
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        st.write(f"Using device: {device}")

        # Chargement des modèles YOLO
        st.write("Chargement du modèle YOLO...")
        coco_model = YOLO('yolov8n.pt')  # Modèle pour la détection des véhicules
        coco_model.to(device)

        license_plate_detector = YOLO('license_plate_detector.pt')  # Modèle pour la détection des plaques
        license_plate_detector.to(device)
        st.write("Chargement du modèle YOLO terminé.")

        # Variables pour le traitement
        results = {}
        mot_tracker = Sort()
        cap = cv2.VideoCapture(input_path)

        # Configuration de la sortie vidéo
        output_path = "./output_video.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        frame_nmr = -1
        ret = True
        st.write("Détection des plaques commencée.")
        while ret:
            frame_nmr += 1
            ret, frame = cap.read()
            if ret:
                # Détection des véhicules
                detections = coco_model(frame, device=device, conf=0.25)[0]  # Ajustez conf si nécessaire
                detections_ = []
                for detection in detections.boxes.data.tolist():
                    x1, y1, x2, y2, score, class_id = detection
                    if int(class_id) in [2, 3, 5, 7]:  # Classes de véhicules
                        detections_.append([x1, y1, x2, y2, score])

                # Suivi des véhicules
                track_ids = mot_tracker.update(np.asarray(detections_))

                # Détection des plaques
                license_plates = license_plate_detector(frame, device=device, conf=0.25)[0]
                for license_plate in license_plates.boxes.data.tolist():
                    x1, y1, x2, y2, score, class_id = license_plate

                    # Attribution des plaques aux véhicules
                    xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)

                    if car_id != -1:
                        # Découper et traiter la plaque
                        license_plate_crop = frame[int(y1):int(y2), int(x1): int(x2), :]
                        license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
                        _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)

                        # Lecture du numéro de plaque
                        license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

                        if license_plate_text is not None:
                            results[frame_nmr][car_id] = {'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
                                                          'license_plate': {'bbox': [x1, y1, x2, y2],
                                                                            'text': license_plate_text,
                                                                            'bbox_score': score,
                                                                            'text_score': license_plate_text_score}}
                # Écrire la frame traitée dans la vidéo de sortie
                out.write(frame)

        cap.release()
        out.release()

        # Afficher la vidéo de sortie
        st.subheader("Résultat de la détection")
        st.video(output_path)

        # Option pour télécharger la vidéo de sortie
        with open(output_path, "rb") as file:
            st.download_button(
                label="Télécharger la vidéo traitée",
                data=file,
                file_name="output_video.mp4",
                mime="video/mp4"
            )

    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")
