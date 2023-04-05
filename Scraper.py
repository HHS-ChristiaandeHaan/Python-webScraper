import requests
from bs4 import BeautifulSoup
import csv

print("Hellow World")

with open('bever_schoenen.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'price', 'description', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

pages_of_url = 4;
list_urls = [];

for i in range(pages_of_url):
    url = 'https://www.bever.nl/c/heren/schoenen/wandelschoenen.html?size=48&page={0}&filter=%2526filter%253Daverage_rating%253A10%253Caverage_rating%253C50'
    url = url.format(i)

    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    product_tags = soup.find_all('div', {'class': 'as-m-product-tile'})


    for tag in product_tags:
        url_product = url.split('?')
        link =  url_product[0] + tag.find('a').get('href')
        list_urls.append(link)
        #print( url_product[0] + list.get('href'))
        #response_product = requests.get(url_product, headers=headers)

    #for tag in product_tags:
    #    name = tag.find('div', {'class': 'as-m-product-tile__title-wrapper'}).text.strip()
    #    price = tag.find('div', {'class': 'as-a-price__value as-a-price__value--sell'}).text.strip()
    #    description = tag.find('div', {'class': 'as-m-product-tile__info-wrapper'}).text.strip()
    #    url_product = url.split('?')
    #    link =  url_product[0] + tag.find('a').get('href')
    #    #print(link)
        #for link in tag.find_all('a'):
        #    print(link.get('href'))
    #    #print("---")
    #    #writer.writerow({'name': name, 'price': price, 'description': description, 'link': link})
    
##for i in list_urls:
#    url = list_urls[i]
#    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#    response = requests.get(url, headers=headers)
#
#    soup = BeautifulSoup(response.content, 'html.parser')
#    product_tags = soup.find_all('div', {'class': 'as-m-product-tile'})
    
print(list_urls[0])