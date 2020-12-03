FROM python:3.6-slim

WORKDIR /user/src/app

COPY requirements.txt ./

RUN apt-get updtae && apt-get install -y \
    python3 \
    python3-pip3 \
    vim \
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python","./app/app.py" ]