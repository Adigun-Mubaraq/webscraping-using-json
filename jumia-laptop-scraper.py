import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.jumia.com.ng/laptops/apple/"
response = requests.get(URL) 

soup = BeautifulSoup(response.content, 'html5lib')

result = []
products = soup.select('article.prd')

for product in products:
    name = product.select_one('h3.name').text
    price = product.select_one('div.prc').text

    result.append({
        'title' : name,
        'price' : price,
    })

with open('./result.json', 'w') as outfile:
  json.dump(result, outfile)
