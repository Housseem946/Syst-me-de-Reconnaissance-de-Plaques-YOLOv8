# Système de Reconnaissance de Plaques-YOLOv8

## Description du Projet

Ce projet, développé dans le cadre de notre module PAS (Projet Académique & Scientifique) lors de notre formation à l'ESILV en Data et Intelligence Artificielle, consiste en une application de reconnaissance automatique des plaques d'immatriculation à partir d'images ou de vidéos (une vidéo dans notre cas).

Ce projet exploite les capacités des modèles de computer vision, en particulier YOLOv8 et OCR, pour détecter et lire les plaques d'immatriculation à partir de vidéos.

## Fonctionnalités

- **Détection des véhicules** : Utilisation de YOLOv8 pré-entraîné pour détecter les véhicules dans une vidéo.
- **Détection des plaques** : Un modèle entraîné sur des données spécifiques pour localiser les plaques d'immatriculation.
- **Reconnaissance des caractères** : Extraction des numéros de plaques à l’aide d’un module OCR (EasyOCR).
- **Interpolation des données manquantes** : Gestion des valeurs manquantes à travers le module add_missing_data.py pour des résultats plus fluides.
- **Visualisation des résultats** : Affichage des détections et des numéros extraits avec une sortie vidéo fluide.
- **Application Streamlit** : Interface utilisateur simple pour tester les vidéos via un système de drag-and-drop et afficher les vidéos résultantes.

## Technologies
- Python
- Ultralytics YOLOv8
- OpenCV
- Tesseract OCR
- Streamlit

## Data 

- La vidéo utilisée dans notre cas pour les tests peut être téléchargée [ici](https://drive.google.com/file/d/1JbwLyqpFCXmftaJY1oap8Sa6KfjoWJta/view).
- Un modèle pré-entraîné YOLOv8n a été utilisé pour détecter les véhicules disponible [ici](https://drive.google.com/file/d/1Zmf5ynaTFhmln2z7Qvv-tgjkWQYQ9Zdw/view).
- Un détecteur de plaques a été entraîné avec le dataset disponible [ici](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4).

## Dépendances

Le projet dépend des modules suivants :

- Python 3.10 : Version utilisée pour le développement.
- Ultralytics YOLOv8 : Modèle de détection d’objets.
- OpenCV : Traitement d’images et affichage des résultats.
- EasyOCR : Reconnaissance des caractères sur les plaques.
- sort : Algorithme de suivi pour le suivi des plaques dans les vidéos(vous devez cloner le dépot en dessous).

### Pour installer et utiliser le module sort, clonez le dépôt suivant (Obligatoire) :

```bash
git clone https://github.com/abewley/sort
```

## Structure du Projet

```
├── sort # Module cloné d'un autre repo permettant le suivi des plaques dans les vidéos
│  
├── add_missing_data.py # interpoler les valeurs manquantes et améliorer les résultats.
├── app.py # fichier Streamlit pour créer une interface utilisateur interactive pour l'application.
├── main.py # générer un fichier test.csv contenant les données détectées
├── util.py #  Contient les fonctions utilitaires pour soutenir les autres fichiers.
├── visualize.py # générer une vidéo contenant les résultats de la détection et de la reconnaissance des plaques.
├── license_plate_detector.pt : Fichier de modèle YOLO pré-entraîné pour détecter les plaques d'immatriculation.
├── yolov8n.pt : # Fichier de modèle YOLOv8 pré-entraîné utilisé pour détecter d'autres objets, comme les véhicules.
│   
├── README.md                   
```

## Installation d'un environnement virtuel  ( Optional )

#### Créer un environnement virtuel :

```bash
python -m venv env
```

#### Activer l’environnement :

```bash
.\env\Scripts\activate
```

## Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Exécution du Projet


#### 1. Application Streamlit 

Lancez l'application Streamlit pour tester vos vidéos via une interface utilisateur :
   
```bash
streamlit run app.py
```

##### Fonctionnalités :

- Drag-and-drop pour télécharger les vidéos.

- Analyse et traitement automatique des vidéos.

- Affichage de la vidéo traitée directement dans l'application.

- Option pour télécharger la vidéo résultante.

#### 2. Détection et extraction initiales : Exécutez le fichier main.py sur une vidéo d'entrée pour générer un fichier test.csv contenant les données détectées.
   
```bash
python main.py
```

#### 3. Interpolation des données manquantes : Exécutez le script add_missing_data.py pour interpoler les valeurs manquantes et améliorer les résultats.

```bash
python add_missing_data.py
```

#### 4. Visualisation finale : Exécutez le script visualize.py pour générer une vidéo contenant les résultats fluides et précis de la détection et de la reconnaissance des plaques.
   
```bash
python visualize.py
```
Vous trouverez le résultat dans le répertoire sous le nom "out.mp4".

## Résultat final du test pour notre exemple

[🎥 Regardez la vidéo ici](https://drive.google.com/file/d/17xrx6mQ1JLJtnywrWrwzypNUjXs7VqxV/view?usp=sharing)

## 📷 Aperçu de l'application


![alt text](<WhatsApp Image 2025-01-17 à 18.10.23_3f098456.jpg>)

#### Étape 1 : Détection et extraction initiales

![alt text](image.png)

#### Étape 2 : Interpolation des données manquantes


#### Étape 3 : Génération de la vidéo finale


Pour toute question, vous pouvez me contacter via LinkedIn : https://www.linkedin.com/in/houssem-rezgui-/

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request pour des améliorations










  

