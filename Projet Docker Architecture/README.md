- [Projet Docker Architecture](#projet-docker-architecture)
  - [1 Lancement du projet](#1-lancement-du-projet)
  - [2 Fonctionnalités](#2-fonctionnalités)
    - [2.1 Lancement Docker](#21-lancement-docker)
    - [2.2 Déploiement sur Heroku](#22-déploiement-sur-heroku)
      - [2.2.1 Installation et configuration de Heroku](#221-installation-et-configuration-de-heroku)
      - [2.2.2 Lien de l'application](#222-lien-de-lapplication)
    - [2.3 Chemins application flask](#23-chemins-application-flask)

# Projet Docker Architecture

## 1 Lancement du projet

## 2 Fonctionnalités

### 2.1 Lancement Docker
Creation de l'image Docker à partir du Dockerfile

`$ docker build -t py-project-docker .`

Vérification des images 

`$ sudo docker images`
![images docker](https://user-images.githubusercontent.com/58144828/132416563-be6ef7b3-fc8f-49dc-a04b-b6ed881a0f5f.PNG)

### 2.2 Déploiement sur Heroku

#### 2.2.1 Installation et configuration de Heroku

`$ sudo snap install --classic heroku`

`$ heroku --version`

`$ heroku login`

`$ heroku login -i`

`$ cd ./Projet Docker Architecture`

`$ heroku create`

#### 2.2.2 Lien de l'application

<https://projet-docker-architecture.herokuapp.com/>

### 2.3 Chemins application flask
