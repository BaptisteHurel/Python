# Couche OS / Définition de l'image utilisée
FROM python:3

WORKDIR /Documents/docker/app

COPY requirements.txt ./

#Execution d'une commande dans le conteneur
RUN apt-get update && apt-get install -y
RUN apt-get install python3
RUN apt-get install python3-pip3
RUN apt-get install vim



RUN npm install