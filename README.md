# Système-de-Reconnaissance-de-Plaques-YOLOv8

## Description du Projet
Ce projet, développé dans le cadre de mon module "Projet Technique & Scientifique" lors de ma formation en école d’ingénieurs en Data et Intelligence Artificielle, est une application de reconnaissance automatique des plaques d'immatriculation à partir des Images/Vdéo . Il utilise les capacités des modèles de **computer vision**, en particulier **YOLOv8** et **OCR**, pour détecter et lire des plaques à partir de vidéos.

Ce projet a été une excellente opportunité pour approfondir mes connaissances en Computer Vision, explorer les modèles YOLO et OCR, et renforcer mes compétences en programmation Python.

## Fonctionnalités

- Détection des véhicules : Utilisation de YOLOv8 pré-entraîné pour détecter les véhicules dans une vidéo.
- Détection des plaques : Un modèle entraîné sur des données spécifiques pour localiser les plaques d'immatriculation.
- Reconnaissance des caractères : Extraction des numéros de plaques à l’aide d’un module OCR (EasyOCR).
- Interpolation des données manquantes : Gestion des valeurs manquantes pour des résultats plus fluides.
- Visualisation des résultats : Affichage des détections et des numéros extraits avec une sortie vidéo fluide.

## Technologies
- Python
- Ultralytics YOLOv8
- OpenCV
- Tesseract OCR

## Data 

- La vidéo utilisée pour les tests peut être téléchargée ici.
- Un modèle pré-entraîné YOLOv8n a été utilisé pour détecter les véhicules.
- Un détecteur de plaques a été entraîné avec le dataset disponible ici.

## Dépendances

Le projet dépend des modules suivants :

- Python 3.10 : Version utilisée pour le développement.
- Ultralytics YOLOv8 : Modèle de détection d’objets.
- OpenCV : Traitement d’images et affichage des résultats.
- EasyOCR : Reconnaissance des caractères sur les plaques.
- sort : Algorithme de suivi pour le suivi des plaques dans les vidéos.

#### Pour installer et utiliser le module sort, clonez le dépôt suivant :

```bash
git clone https://github.com/abewley/sort
```

## Installation

#### Créer un environnement virtuel :

```bash
conda create --prefix ./env python=3.10 -y
```

#### Activer l’environnement :

```bash
source activate ./env
```

#### Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Exécution du Projet

1. Détection et extraction initiales : Exécutez le fichier main.py sur une vidéo d'entrée pour générer un fichier test.csv contenant les données détectées.
   
```bash
python main.py
```

2. Interpolation des données manquantes : Exécutez le script add_missing_data.py pour interpoler les valeurs manquantes et améliorer les résultats.

```bash
python add_missing_data.py
```

3. Visualisation finale : Exécutez le script visualize.py pour générer une vidéo contenant les résultats fluides et précis de la détection et de la reconnaissance.
   
```bash
python visualize.py
```









  

