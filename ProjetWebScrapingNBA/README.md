# Projet Web Scraping
## Sujet :
Récupération du meilleur scoreur et de son nombre de points sur une saison NBA.

### Site scrapé:
https://fr.wikipedia.org/wiki/Liste_des_meilleurs_marqueurs_en_NBA_par_saison

### Données scrapés: 
- Season
- Player
- Nb Point

## Déploiement et lancement sur Docker
- docker-compose up --build -d
- docker exec scraping_nba_container python3 main.py

L'image du graphique sera présente dans le dossier data/results