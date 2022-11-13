import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

titres_bs = soup.find_all('a')

titres = []

for titre in titres_bs:
    titres.append(titre.string)
    print(titres)