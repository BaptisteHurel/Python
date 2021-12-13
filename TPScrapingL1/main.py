from bs4 import BeautifulSoup
import requests
import pandas as pd

#ETAPE 1
url = "https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020"
request_text = requests.get(url)
#print(request_text.content)

#ETAPE 2
soup = BeautifulSoup(request_text.content, 'html5lib')

#ETAPE 3
print("Il y a {} balises Table".format(len(soup.find_all('table'))))

#print(soup.find('table'))
#print(soup.find_all)

#ETAPE 4
all_tables = soup.find_all('table')
all_tables[:2]

#ETAPE 5
teams = soup.find('table',class_= 'DebutCarte')
#print(teams)

#ETAPE 6
clubs = teams.find_all('a')[:5]

#ETAPE 6 bis
for club in clubs:
    if club.find("img"):
        continue
    else : 
        print(club)

#ETAPE 7
print("Clubs \n")
for club in clubs:
    if club.find('img'):
        continue
    else:
        print(club.get_text())

print("\n -- \n" + "URL \n")

for club in clubs:
    if club.find('img'):
        continue
    else:
        print(club.get('href'))

#ETAPE 8
df = pd.DataFrame(columns=['Club','URL'])

for club in clubs:
    if club.find('img'):
        continue
    else:
        df = df.append({'Club': club.getText(),'URL': club.get('href')}, ignore_index=True)


clubs = soup.find('table', "DebutCarte").find_all('a')

full_df = pd.DataFrame(columns=['Club', 'URL'])

for club in clubs:
    if club.find('img'):
        continue
    else:
        full_df = full_df.append({'Club': club.getText(),'URL': club.get('href')}, ignore_index=True)

full_df.head()

full_df.to_csv('ClubsL1.csv')
full_df.to_excel('ClubsL1.xls')
