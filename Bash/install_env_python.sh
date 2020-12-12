#!/bin/bash

sudo apt update &&
sudo apt install software-properties-common &&
sudo add-apt-repository ppa:deadsnakes/ppa &&
sudo apt-get install -y python3.8 &&
sudo apt-get install -y python3-pip &&
python3.8 --version &&
sudo apt install python3-venv &&
python3 -m venv env &&
source env/bin/activate &&

pip3 install jupyter \
        numpy \
        notebook \
        pandas \
        scikit-learn \
        seaborn \
        fastapi \
               uvicorn \
        joblib \
        matplotlib \
        stop_words \
        streamlit \
        flask &&
sudo apt-get install -y docker