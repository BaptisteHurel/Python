- [Projet Docker Architecture](#projet-docker-architecture)
  - [1 Lancement du projet](#1-lancement-du-projet)
  - [2 Fonctionnalités](#2-fonctionnalités)
    - [2.1 Lancement Docker](#21-lancement-docker)
    - [2.2 Déploiement sur Heroku](#22-déploiement-sur-heroku)
      - [2.2.1 Installation et configuration de Heroku](#221-installation-et-configuration-de-heroku)
      - [2.2.2 Lien de l'application](#222-lien-de-lapplication)
    - [2.3 Chemins application flask](#23-chemins-application-flask)

# Projet Docker Architecture

## 1 Présentation du projet
### 1.1 Description
### 1.2 Architecture fonctionnelle
### 1.3 : Lancement du projet

## 2 Fonctionnalités

### 2.1 Lancement Docker

Creation de l'image Docker à partir du Dockerfile

`$ sudo docker build -t py-app-projet-docker .`

Vérification des images

`$ sudo docker images`

Ajout de l'image dans un conteneur

`$ sudo docker run 0f615f28df5c`

`$ sudo docker build -t 0f615f28df5c .`

`$ sudo docker run -d -p 5000:5000 455dd8c21be0`

#### (9523c8323810b63533e3837e42592bb6666e2c49f6d3d8c71555ab83d07a46fa)

Vérification des conteneurs 

`$ sudo docker ps`

#### 2.1.2  Docker Swarm Rocks
`$ sudo docker swarm init`

`$ sudo docker node ls`

#### 2.1.2  Traefik Proxy
`$ docker network create --driver=overlay traefik-public`


### 2.2 Déploiement sur Heroku

#### 2.2.1 Installation et configuration de Heroku

`$ sudo snap install --classic heroku`

`$ heroku --version`

`$ heroku login`

`$ heroku login -i`

`$ cd ./Projet Docker Architecture`

`$ heroku create`

#### 2.2.2 Lien de l'application sur Heroku

<https://projet-docker-architecture.herokuapp.com/>


### 2.3 Chemins application flask

LOCALHOST : http://0.0.0.0:5000/ ou http://172.17.0.2:5000/
`$ cd ./Documents/'Projet Docker Architecture'/ml_template_api/docker`
`$ python app.py`

HEROKU : https://projet-docker-architecture.herokuapp.com/
