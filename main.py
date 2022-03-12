import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = 'https://store.steampowered.com/search/?term=gta'

def get_data(url):
    r = requests.get(url)
    return r.text

#prosessing data
def parse(data):
    result = []
    soup = BeautifulSoup(data, 'html.parser')
    contents = soup.find('div',attrs={id:'search_resultsRows'})
    games = contents.find_all('a')

    print(result)

