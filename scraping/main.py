import requests
import json
import csv
from bs4 import BeautifulSoup

url = 'https://www.rabota.md/search/?query=python&searchType=1&cityID=1'

page = requests.get(url, stream=True)
soup = BeautifulSoup(page.content, 'html.parser')

jobs = soup.find_all('div', {'class':'preview'} )
data = []
for job in jobs:
    h3 = job.find('h3')
    company_data = job.find('div')
    if h3 and company_data:
        title = h3.find_all('a', class_='vacancy')[0].text
        company_data = job.find('div').text.replace('\n', '').split('•')
        company, location = company_data[-2], company_data[-1]
        company = company.strip()
        location = location.strip()
        description = job.find('p').text.replace('\n', ' ').strip()
        salary = job.find_all('span')[-1].text.replace('\n', '').strip()
        data.append({
            'title': title,
            'company': company,
            'location': location,
            'description': description,
            'salary': salary
        })

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    keys = data[0].keys()
    dict_writer = csv.DictWriter(f, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)

import json

with open('jobs.json', 'w') as json_file:
    json.dump(data, json_file)