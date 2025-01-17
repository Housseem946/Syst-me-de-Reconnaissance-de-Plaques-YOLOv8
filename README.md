# Système de Reconnaissance de Plaques-YOLOv8

## Description du Projet

Ce projet, développé dans le cadre de notre module PAS (Projet Académique & Scientifique) lors de notre formation à l'ESILV en Data et Intelligence Artificielle, consiste en une application de reconnaissance automatique des plaques d'immatriculation à partir d'images ou de vidéos (une vidéo dans notre cas).

Ce projet exploite les capacités des modèles de computer vision, en particulier YOLOv8 et OCR, pour détecter et lire les plaques d'immatriculation à partir de vidéos.

## Fonctionnalités

<<<<<<< HEAD
- **Détection des véhicules** : Utilisation de YOLOv8 pré-entraîné pour détecter les véhicules dans une vidéo.
- **Détection des plaques** : Un modèle entraîné sur des données spécifiques pour localiser les plaques d'immatriculation.
- **Reconnaissance des caractères** : Extraction des numéros de plaques à l’aide d’un module OCR (EasyOCR).
- **Interpolation des données manquantes** : Gestion des valeurs manquantes à travers le module add_missing_data.py pour des résultats plus fluides.
- **Visualisation des résultats** : Affichage des détections et des numéros extraits avec une sortie vidéo fluide.
- **Application Streamlit** : Interface utilisateur simple pour tester les vidéos via un système de drag-and-drop et afficher les vidéos résultantes.
=======
- Détection des véhicules : Utilisation de YOLOv8 pré-entraîné pour détecter les véhicules dans une vidéo.
- Détection des plaques : Un modèle entraîné sur des données spécifiques pour localiser les plaques d'immatriculation.
- Reconnaissance des caractères : Extraction des numéros de plaques à l’aide d’un module OCR (EasyOCR).
- Interpolation des données manquantes : Gestion des valeurs manquantes à travers le module add_missing_data.py pour des résultats plus fluides.
- Visualisation des résultats : Affichage des détections et des numéros extraits avec une sortie vidéo fluide.
>>>>>>> 510ea9165240081ef08d68d05793670669dcb7d5

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
<<<<<<< HEAD
- sort : Algorithme de suivi pour le suivi des plaques dans les vidéos(vous devez cloner le dépot en dessous).

### Pour installer et utiliser le module sort, clonez le dépôt suivant (Obligatoire) :
=======
- sort : Algorithme de suivi pour le suivi des plaques dans les vidéos.

#### Pour installer et utiliser le module sort, clonez le dépôt suivant :
>>>>>>> 510ea9165240081ef08d68d05793670669dcb7d5

```bash
git clone https://github.com/abewley/sort
```

<<<<<<< HEAD
## Structure du Projet

```
├── notebooks 
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
=======
## Installation
>>>>>>> 510ea9165240081ef08d68d05793670669dcb7d5

#### Créer un environnement virtuel :

```bash
python -m venv env
```

#### Activer l’environnement :

```bash
.\env\Scripts\activate
```

<<<<<<< HEAD
## Installer les dépendances :
=======
#### Installer les dépendances :
>>>>>>> 510ea9165240081ef08d68d05793670669dcb7d5

```bash
pip install -r requirements.txt
```

## Exécution du Projet

<<<<<<< HEAD

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
=======
1. Détection et extraction initiales : Exécutez le fichier main.py sur une vidéo d'entrée pour générer un fichier test.csv contenant les données détectées.
>>>>>>> 510ea9165240081ef08d68d05793670669dcb7d5
   
```bash
python main.py
```

<<<<<<< HEAD
#### 3. Interpolation des données manquantes : Exécutez le script add_missing_data.py pour interpoler les valeurs manquantes et améliorer les résultats.
=======
2. Interpolation des données manquantes : Exécutez le script add_missing_data.py pour interpoler les valeurs manquantes et améliorer les résultats.
>>>>>>> 510ea9165240081ef08d68d05793670669dcb7d5

```bash
python add_missing_data.py
```

<<<<<<< HEAD
#### 4. Visualisation finale : Exécutez le script visualize.py pour générer une vidéo contenant les résultats fluides et précis de la détection et de la reconnaissance des plaques.
=======
3. Visualisation finale : Exécutez le script visualize.py pour générer une vidéo contenant les résultats fluides et précis de la détection et de la reconnaissance.
>>>>>>> 510ea9165240081ef08d68d05793670669dcb7d5
   
```bash
python visualize.py
```
<<<<<<< HEAD
Vous trouverez le résultat dans le répertoire sous le nom "out.mp4".

## Résultat final du test pour notre exemple
=======

## Résultat final du test 
>>>>>>> 510ea9165240081ef08d68d05793670669dcb7d5

[🎥 Regardez la vidéo ici](https://drive.google.com/file/d/17xrx6mQ1JLJtnywrWrwzypNUjXs7VqxV/view?usp=sharing)










  

