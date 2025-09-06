# LITRevu

Projet Openclassrooms : P9 Développez une application Web en utilisant Django

## Présentation du projet

LITRevu est une application web développée avec Django permettant aux utilisateurs de :
- publier des **tickets de lecture** (demandes de critique),
- poster des **critiques de livres** (réponses à un ticket ou critiques libres),
- **suivre** d'autres utilisateurs pour voir leurs publications dans un fil d’actualité personnalisé.

Ce projet a été réalisé dans le cadre de la formation “Développeur d'application Python” – OpenClassrooms.

---

## Installation et prérequis

### Prérequis

- Python 3.13.2
- pip
- virtualenv

### Installation

```bash
# Cloner le dépôt
git clone https://github.com/Faaab84/projet_9_LITRevu.git
cd litrevu

# Créer et activer un environnement virtuel
python -m venv env
source env/bin/activate  # ou env\Scripts\activate sous Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur local
python manage.py runserver

Accéder à l'application à l’adresse : http://localhost:8000/login
```

##  Style & CSS

Le projet utilise :

atière d’accessibilité, ce qui facilite la conformité aux normes WCAG.
- Des variables SCSS personnalisées (couleurs, contrastes, boutons…)
- Les fichiers CSS personnalisés sont situés dans static/css/styles.css.



## Technologies utilisées & qualité du code

- Python 3.10.12
- Django 5.2.1
- SQLite (base intégrée pour test local)
- Bootstrap 
- Pillow (upload images)
- Flake8 pour la vérification PEP8
- Lighthouse pour vérifier l’accessibilité (WCAG)

###  Qualité du code
- Vérification de conformité avec flake8
- Fichier .flake8 pour paramétrer flake8

##  Données de test

Une base de données est intégrée afin de permettre les tests, voici les utilisateurs : 
- root (administrateur) : root
- Paul : password123*
- Jean : password124*
- fabien : erty159*



## Auteur
Projet réalisé par Faaab84 en septembre 2025.