# Projet Docker Architecture
- [Projet Docker Architecture](#projet-docker-architecture)
  - [1 Présentation du projet](#1-présentation-du-projet)
    - [1.1 Description](#11-description)
    - [1.2 Schéma Architecture Fonctionnelle](#12-schéma-architecture-fonctionnelle)
    - [1.3 Lancement du projet](#13-lancement-du-projet)
  - [2 Fonctionnalités](#2-fonctionnalités)
    - [2.1 Lancement Docker](#21-lancement-docker)
      - [2.1.1 Images et Conteneurs](#211-images-et-conteneurs)
      - [2.1.2 Docker Swarm Rocks](#211-docker-swarm-rocks)
      - [2.1.3 Traefik Proxy](#213-traefik-proxy)
    - [2.2 Déploiement sur Heroku](#22-déploiement-sur-heroku)
      - [2.2.1 Installation et configuration de Heroku](#221-installation-et-configuration-de-heroku)
      - [2.2.2 Lien de l'application sur Heroku](#222-lien-de-lapplication-sur-heroku)
    - [2.3 Chemins application flask](#23-chemins-application-flask)
    - [2.4 Base de donnée MySQL](#24-base-de-donnée-mysql)
    - [2.5 Fichier de test](#24-fichier-de-test)
      - [2.5.1 Ajout dans le fichier docker-compose.yml](#221-ajout-dans-le-fichier-docker-compose.yml)

------------------------------------------------------------------------------------------------------------
## 1 Présentation du projet
### 1.1 Description
Ce projet est une **application Flask** avec un accès à une **base de donnée MySQL**, elle permet d'afficher les statistiques de matchs de basket de NBA.
Cette application est déployée sur **Heroku** pour être accesible en ligne et **containerisée avec Docker**.

### 1.2 Schéma Architecture fonctionnelle

![image](https://user-images.githubusercontent.com/58144828/132656422-a4dd070a-6ee2-416c-8ead-398940cc84f4.png)


### 1.3 : Lancement du projet
Lien sur Heroku : https://projet-docker-architecture.herokuapp.com/

## 2 Fonctionnalités

### 2.1 Lancement Docker
#### 2.1.1 Images et Conteneurs
Creation de l'image Docker à partir du Dockerfile

`$ docker build -t py-app-projet-docker .`

`$ docker build -t app-docker-project .`

Vérification des images

`$ docker images`
![images docker](https://user-images.githubusercontent.com/58144828/132645427-fbe84cfa-8607-4959-b43e-12175eabb5c3.PNG)
![image](https://user-images.githubusercontent.com/58144828/132826630-22a86858-dd07-48bf-9434-d9bbf353b762.png)


Ajout de l'image dans un conteneur

`$ docker run 0f615f28df5c`

`$ docker build -t 0f615f28df5c .`

`$ docker run -d -p 5000:5000 455dd8c21be0`

#### (9523c8323810b63533e3837e42592bb6666e2c49f6d3d8c71555ab83d07a46fa)

Vérification des conteneurs 

`$ docker ps`
![conteneurs docker](https://user-images.githubusercontent.com/58144828/132645736-ce2c7d88-c4ec-4948-ba90-b0eb9d783db2.PNG)

#### 2.1.2  Docker Swarm Rocks

Procédure à suivre : <https://dockerswarm.rocks/>

`$ docker swarm init`

`$ docker node ls`
![docker node ls](https://user-images.githubusercontent.com/58144828/132645994-109b181f-2ca7-437a-b8e5-21342cb447d3.PNG)

#### 2.1.3  Traefik Proxy

Procédure à suivre : <https://dockerswarm.rocks/traefik/>

`$ docker network create --driver=overlay traefik-public`
![network traefik](https://user-images.githubusercontent.com/58144828/132645505-38e7e0b4-1c8b-41e9-be50-173fb2958485.PNG)


### 2.2 Déploiement sur Heroku

#### 2.2.1 Installation et configuration de Heroku

`$ snap install --classic heroku`

`$ heroku --version`

`$ heroku login`
![heroku login](https://user-images.githubusercontent.com/58144828/132645791-3b250a20-6a9a-40e4-b530-b862168afd14.PNG)

`$ heroku login -i`

`$ cd ./Projet Docker Architecture`

`$ heroku create`
![heroku create](https://user-images.githubusercontent.com/58144828/132645810-01d08f89-8852-4bd7-a949-740c1eaea513.PNG)

#### 2.2.2 Lien de l'application sur Heroku

<https://projet-docker-architecture.herokuapp.com/>


### 2.3 Chemins application flask

LOCALHOST : http://0.0.0.0:5000/ ou http://172.17.0.2:5000/

`$ cd ./Documents/'Projet Docker Architecture'/ml_template_api/docker`

`$ python app.py`

HEROKU : https://projet-docker-architecture.herokuapp.com/

### 2.4 Base de donnée MySQL
MYSQL Database
```
+-----------------------+
| Table Players         |
+-----------------------+
| Player                |
| height                |
| weight                |
| collage               |
| born                  |
| birth_city            |
| birth_state           |
+-----------------------+

+-----------+------------------+
| host      | user             |
+-----------+------------------+
| %         | root             |
| localhost | mysql.infoschema |
| localhost | mysql.session    |
| localhost | mysql.sys        |
| localhost | root             |
+-----------+------------------+
```

**Test d'accès aux données de la base donnée**

![image](https://user-images.githubusercontent.com/58144828/132832185-a0b28bc0-1ea8-4b9f-98c4-d1c46d0dc04d.png)

### 2.5 Fichier de test

#### 2.5.1 Ajout dans le fichier docker-compose.yml

![image](https://user-images.githubusercontent.com/58144828/135060159-487aca49-e41d-43d3-b63d-50d4b7e59263.png)
