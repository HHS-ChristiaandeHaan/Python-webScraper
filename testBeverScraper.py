import requests
from bs4 import BeautifulSoup
import csv
from random import randint
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



url = 'https://www.bever.nl/p/meindl-san-francisco-gore-tex-wandelschoen-HABFC70002.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# load the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url);

cookieButton = driver.find_element(By.ID, "accept-all-cookies")
cookieButton.click()

time.sleep(2)

reviewButton = driver.find_element(By.CLASS_NAME, "as-m-group as-m-group--gutter as-m-group--inline as-m-group--align-space-between as-m-group--valign-center")
reviewButton.click()

time.sleep(2)

# page_source is a variable created by Selenium - it holds all the HTML
page = driver.page_source

#response = requests.get(url, headers=headers)

soup = BeautifulSoup(page, 'html.parser')

product_tags = soup.find_all('div', {'class': 'product-detail base-component-ssr parbase'})

time.sleep(20)

for tag in product_tags:
    #merk = tag.find('a', {'class' : 'as-a-link as-a-link--base'}).text.strip()
    name = tag.find('h1', {'class': 'as-a-heading as-a-heading--title'}).text.strip()
    price = tag.find('div', {'class': 'as-a-price__value as-a-price__value--sell'}).text.strip()
    description = tag.find('div', {'class': 'as-t-box margin-bottom-mobile-1'}).text.strip()
    print (name +" "+ price +" "+ description)

    images = tag.findAll('div', {'class': 'swiper-wrapper'})
    foto = [];

    for i in images:
        image = i.find('img').attrs['src']
        foto.append(image)

    response = requests.get("https:" + foto[1])
    # Schrijf de inhoud van de response weg naar een lokale bestand
    bestandsnaam =  f'imgs/{name}.jpg'   
    with open(bestandsnaam, 'wb') as f:
                f.write(response.content)
    print(f'Afbeelding opgeslagen als {bestandsnaam}.')

    #writer.writerow({'name': name, 'price': price, 'description': description})

driver.quit()
