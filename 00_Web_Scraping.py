import requests
import os
from bs4 import BeautifulSoup
import urllib.request

# Initialize
Folder = "impressionismus"
site = 'https://www.kunstbilder-galerie.de/kunstdrucke.html?p=4&painting_style=1927'
response = requests.get(site)
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')


# Download all Images
for i in img_tags:
        urllib.request.urlretrieve(i['data-amsrc'], filename = Folder + "/" + i['data-amsrc'].split('/')[-1])

# Delete other files
for file in os.listdir(Folder):
    if file.endswith('.png') or file.endswith('.gif'):
        os.remove(Folder + "/" + file)

try:
    os.remove(Folder + "/" + "home-kunstdrucke.jpg")
    os.remove(Folder + "/" + "sehr-gut.jpg")
    os.remove(Folder + "/" + "h-" + Folder +".jpg")
except:
    print("Löschung fehlgeschlagen")
finally:
    print("WebScraping abgeschlossen!")
