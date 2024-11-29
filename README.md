# Système de Reconnaissance de Plaques-YOLOv8

## Description du Projet

Ce projet, développé dans le cadre de mon module "Projet Technique & Scientifique" lors de ma formation en école d’ingénieurs en Data et Intelligence Artificielle, est une application de reconnaissance automatique des plaques d'immatriculation à partir des Images/Vdéo . Il utilise les capacités des modèles de **computer vision**, en particulier **YOLOv8** et **OCR**, pour détecter et lire des plaques à partir de vidéos.

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

- La vidéo utilisée dans notre cas pour les tests peut être téléchargée [ici](https://drive.google.com/file/d/1JbwLyqpFCXmftaJY1oap8Sa6KfjoWJta/view).
- Un modèle pré-entraîné YOLOv8n a été utilisé pour détecter les véhicules disponible [ici](https://drive.google.com/file/d/1Zmf5ynaTFhmln2z7Qvv-tgjkWQYQ9Zdw/view).
- Un détecteur de plaques a été entraîné avec le dataset disponible [ici](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4).

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
python -m venv env
```

#### Activer l’environnement :

```bash
.\env\Scripts\activate
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









  

