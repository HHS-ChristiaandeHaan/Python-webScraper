import requests
from bs4 import BeautifulSoup
import csv

print("Start")

pages_of_url = 1;
list_urls = [];

with open('bever_schoenen.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'price', 'description', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
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

    index = 0
    for i in list_urls:
        url = list_urls[index]
        index+=1
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.content, 'html.parser')
        #get the things on the page. 
        product_tags = soup.find_all('div', {'class': 'product-detail base-component-ssr parbase'})



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


            writer.writerow({'name': name, 'price': price, 'description': description, 'link': link})    
