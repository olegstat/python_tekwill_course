import requests
from bs4 import BeautifulSoup
import json

#Getting the url content
url = 'https://999.md/ru/list/phone-and-communication/mobile-phones?view_type=detail'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all(class_='ads-list-detail-item')

#Looping through the content and saving the extracted data
data = []
for result in results:
  try:
    description = result.find(class_='ads-list-detail-item-intro').text
  except AttributeError:
    description = "No Description"
  title = result.find(class_='ads-list-detail-item-title').text
  price = result.find(class_='ads-list-detail-item-price').text
  description = description.replace('\n', " ")
  description = description.replace('\t', " ")
  data.append({
    'title': title,
    'price': price,
    'description': description
  })

#Exporting the data in JSON
with open('ads.json', 'w', encoding='utf8', newline="") as f:
  json.dump(data, f, ensure_ascii=False)
  print("Saving Complete")
