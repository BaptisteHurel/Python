FROM mysql:latest

COPY ./bdd.sql /docker.entrypoint-initdb.d

ENV MYSQL_DATABASE classicmodels
ENV MYSQL_USER baptiste
ENV MYSQL_PASSWORD baptiste
ENV MYSQL_ROOT_PASSWORD rootpass

EXPOSE 3306