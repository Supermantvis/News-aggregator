from bs4 import BeautifulSoup
import requests
import random
import re
import os
from pprint import pprint


# response = requests.get('https://www.delfi.lt/sportas/sprintas')
# if response.status_code == 200:
#     rspn_content = response.content
# soup = BeautifulSoup(rspn_content, 'html.parser')

# all_headlines = soup.find_all('a')
# for link in all_headlines:
#     print(link.get('href'))


categories = ['krepsinis', 'sportas/tenisas', 'sportas/f1', 'sportas/sprintas']
links_list = []
for catt in categories:
    response = requests.get(f'https://www.delfi.lt/{catt}')
    if response.status_code == 200:
        rspn_content = response.content
    soup = BeautifulSoup(rspn_content, 'html.parser')

    all_headlines = soup.find_all('a')
    for link in all_headlines:
        if link.get('href') is not None and len(link.get('href')) > 65:
            links_list.append('https://www.delfi.lt' + str(link.get('href')))
links_list = set(links_list)


for link in links_list:
    response = requests.get(link)
    if response.status_code == 200:
        rspn_content = response.content
    soup = BeautifulSoup(rspn_content, 'html.parser')

    source_url = link[:20]
    source_name = link[10:20]
    title = soup.title.string
    published_at = soup.find('div', class_='C-article-info__publish-date').text
    description = soup.find('div', class_="C-fragment C-fragment-html C-fragment-html--text").text
    image = soup.find('meta', property='og:image')['content']

    with open("output.txt", "a") as file:
        file.write(source_url)
        file.write(source_name)
        file.write(title)
        file.write(published_at)
        file.write(description)
        file.write(image)




