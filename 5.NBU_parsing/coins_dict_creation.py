import requests
import json
from bs4 import BeautifulSoup


url_ = 'https://coins.bank.gov.ua/moneti-z-neizil-beru/c-451.html'

req = requests.get(url_)
src = req.text

with open('coins.html', 'w', encoding='utf-8-sig') as file:
    file.write(src)

with open('coins.html', encoding='utf-8-sig') as file:
    src_ = file.read()

soup = BeautifulSoup(src_, 'lxml')
all_coins = soup.find_all(class_='model_product')

all_coins_dict = {}
for item in all_coins:
    item_text = item.text
    item_link = 'https://coins.bank.gov.ua' + item.get('href')
    all_coins_dict[item_text] = item_link

with open('all_coins_dict.json', 'w', encoding='utf-8-sig') as file:
    json.dump(all_coins_dict, file, indent=4, ensure_ascii=False)