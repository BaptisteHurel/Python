FROM python:3.6-slim

WORKDIR /user/src/app

COPY requirements.txt ./

#Execution d'une commande dans le conteneur
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip3 \
    vim \
RUN pip install -r requirement.txt

COPY . .

EXPOSE 5000

CMD ["python","./app/app.py"]