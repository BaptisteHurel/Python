FROM python3.8

WORKDIR /app

COPY ./app .

RUN pip3 install -R requirements.txt && mkdir results

CMD ["python3", "app/main.py"]