import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

titres_bs = soup.find_all('a')

titres = []

for titre in titres_bs:
    titres.append(titre.string)
    print(titres)

en_tete = ["lien"]
with open('data.csv', 'w') as fichier_csv:
    write = csv.writer(fichier_csv, delimiter=',')
    write.writerow(en_tete)

    for liens in titres:
        write.writerow([liens])