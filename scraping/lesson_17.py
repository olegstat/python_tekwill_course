import requests
import json
import csv
from bs4 import BeautifulSoup

url = 'https://www.rabota.md/search/?query=python&searchType=1&cityID=1'

page = requests.get(url, stream=True)
soup = BeautifulSoup(page.content, 'html.parser')