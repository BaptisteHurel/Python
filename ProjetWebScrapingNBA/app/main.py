#!/usr/bin/env python
# coding: utf-8

#Import librairies
from datetime import datetime
from bs4 import BeautifulSoup # pour scraper les données
from models.Stats import Stats # Import classe Stats
import requests # code source de la page web
import pandas as pd
import matplotlib.pyplot as plot
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--number", type=int, help="Classement par saisons des meilleurs scoreurs")
args = parser.parse_args()

time.sleep(1)

# Recupération du code source et placement dans une variable 'request_text'
url = "https://fr.wikipedia.org/wiki/Liste_des_meilleurs_marqueurs_en_NBA_par_saison"
request_text = requests.get(url)

# Instantiation de BeautifulSoup 
soup = BeautifulSoup(request_text.content, 'html.parser')

#Trouve les données et les sauvegardes dans une liste 'stats'
stats = soup.find('div',class_= 'wikitable sortable jquery-tablesorter').find_all("div", class_="mw-redirect")
print(stats)

df = pd.DataFrame(columns=["player", "season", "nb_point"])
print(df)

for stat in stats:
    if stat.find("a"):
        url = stat.find("title").get("data-src")
        str_nb_point = str.split(stat.find("td").getText(),"(")
        nb_point = int(str.split(str_nb_point[1]," "[0]))
        player = stat.find("a").getText()[1]
        season = stat.find("a").getText()[0]
        df = df.append(Stats.to_dict(player=player, season=season, nb_point=nb_point), ignore_index=True)

#Récupere chaque saison et son nombre de points associés
def getRank(df : pd.DataFrame, x):
    df = df.head(x)
    df = df.sort_values(by=["nb_point"], ascending=True)
    df.plot.bar(x="season", y="nb_point", rot=80, title="Meilleurs marqueurs de NBA par saison")
    #plot.show(block=True)
    plot.savefig(f"results/rank_{datetime.now.isoformat()}.png", bbox_inches="tight")
    print(df.to_dict)

#Taille du classement voulu //--number pour une taille spécifique
if args.number:
    getRank(df, args.number)
else:
    getRank(df, 20)