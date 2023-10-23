import requests
import json
import csv
from bs4 import BeautifulSoup

with open('all_coins_dict.json', encoding='utf-8-sig') as file:
    all_coins_categories = json.load(file)

iter_count = int(len(all_coins_categories)) - 1
count = 0
print(f'Total number of iterations: {iter_count}')

for category_name, category_href in all_coins_categories.items():

    req_ = requests.get(url=category_href)
    res = req_.text

    with open(f'data/{count}_{category_name}.html', 'w', encoding='utf-8-sig') as file:
        file.write(res)

    with open(f'data/{count}_{category_name}.html', encoding='utf-8-sig') as file:
        res = file.read()

    soup = BeautifulSoup(res, 'lxml')

    # Since the coin is yet to be released, its information continues to be supplemented.
    skip_ = soup.find(href="https://coins.bank.gov.ua/narodzhenij-v-ukrajini-u-suvenirnij-upakovci-n-/p-930.html")
    if skip_ is not None:
        continue

    price = 'Ціна'

    characteristics_categories = soup.find(id='tab-characteristics').find('div').find_all('span')
    denomination = characteristics_categories[0].text
    year_of_minting = characteristics_categories[1].text
    diameter = characteristics_categories[2].text
    circulation = characteristics_categories[3].text
    issuance = characteristics_categories[4].text
    metal_mark = characteristics_categories[5].text
    batch = characteristics_categories[6].text
    metal_name = characteristics_categories[7].text
    artist = characteristics_categories[8].text
    minting_quality = characteristics_categories[9].text
    wholesale = characteristics_categories[10].text
    sculptor = characteristics_categories[11].text
    reverse_desc = characteristics_categories[12].text
    obverse_desc = characteristics_categories[13].text

    with open(f'data/{count}_{category_name}.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            (
                denomination,
                price,
                year_of_minting,
                diameter,
                circulation,
                issuance,
                metal_mark,
                batch,
                metal_name,
                artist,
                minting_quality,
                wholesale,
                sculptor,
                reverse_desc,
                obverse_desc
            )
        )

    price_content = soup.find(class_='new_price_card_product').contents[0]

    characteristics_content = soup.find(id='tab-characteristics').find('div').find_all(class_='char-right')
    denomination_content = characteristics_content[0].text
    year_of_minting_content = characteristics_content[1].text
    diameter_content = characteristics_content[2].text
    circulation_content = characteristics_content[3].text
    issuance_content = characteristics_content[4].text
    metal_mark_content = characteristics_content[5].text
    batch_content = characteristics_content[6].text
    metal_name_content = characteristics_content[7].text
    artist_content = characteristics_content[8].text
    minting_quality_content = characteristics_content[9].text
    wholesale_content = characteristics_content[10].text
    sculptor_content = characteristics_content[11].text
    reverse_desc_content = characteristics_content[12].text
    obverse_desc_content = characteristics_content[13].text

    with open(f'data/{count}_{category_name}.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            (
                denomination_content,
                price_content,
                year_of_minting_content,
                diameter_content,
                circulation_content,
                issuance_content,
                metal_mark_content,
                batch_content,
                metal_name_content,
                artist_content,
                minting_quality_content,
                wholesale_content,
                sculptor_content,
                reverse_desc_content,
                obverse_desc_content
            )
        )

    count += 1