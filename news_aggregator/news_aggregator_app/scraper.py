from bs4 import BeautifulSoup
import requests
from datetime import datetime, date
import re
from . models import Category, NewsArticle

def date_formating(some_date):
    ru_months = {
        'Январь': 1,
        'Февраль': 2,
        'Март': 3,
        'Апрель': 4,
        'Май': 5,
        'Июнь': 6,
        'Июль': 7,
        'Август': 8,
        'Сентябрь': 9,
        'Октябрь': 10,
        'Ноябрь': 11,
        'Декабрь': 12
        }
    
    lt_months = {
        'sausio': 1,
        'vasario': 2,
        'kovo': 3,
        'balandžio': 4,
        'gegužės': 5,
        'birželio': 6,
        'liepos': 7,
        'rugpjūčio': 8,
        'rugsėjo': 9,
        'spalio': 10,
        'lapkričio': 11,
        'gruodžio': 12
        }
    
    pattern = r"(\d{4}) m\.\s+(\w+)\s+(\d+)"
    match = re.search(pattern, some_date)
    year = match.group(1)
    month = match.group(2)
    day = match.group(3)
    if '\u0410' <= month <= '\u044F':
        formated_date = date(int(year), ru_months[month.capitalize()], int(day))
    elif month[0].isupper():
        date_object = datetime.strptime(f"{year} {month} {day}", "%Y %B %d")
        formated_date = date_object.strftime("%Y-%m-%d")
    else:
        formated_date = date(int(year), lt_months[month], int(day))
    return formated_date


def scraper():
    stuff = ['krepsinis', 'sportas/tenisas', 'sportas/f1', 'sportas/sprintas']
    links_list = []
    for catt in stuff:
        response = requests.get(f'https://www.delfi.lt/{catt}')
        if response.status_code == 200:
            rspn_content = response.content
        soup = BeautifulSoup(rspn_content, 'html.parser')

        all_headlines = soup.find_all('a')
        for link in all_headlines:
            if link.get('href') is not None and len(link.get('href')) > 65:
                links_list.append('https://www.delfi.lt' + str(link.get('href')))
    links_list = set(links_list)
    links_list = list(links_list)


    for link in links_list:
        response = requests.get(link)
        if response.status_code == 200:
            rspn_content = response.content
        soup = BeautifulSoup(rspn_content, 'html.parser')
        try:
            source_url = link
            source_name = link[8:20]
            title_ = soup.title.string
            published_at = soup.find('div', class_='C-article-info__publish-date').text
            published_at = date_formating(published_at)
            description = soup.find('div', class_="C-fragment C-fragment-html C-fragment-html--text").text
            image = soup.find('meta', property='og:image')['content']
        except:
            continue
        some_article = NewsArticle.objects.create(
            title=title_,
            description=description,
            source_name=source_name,
            source_url=source_url,
            image=image,
            published_at=published_at,
            )
        some_category = Category.objects.get(name="Sport")
        some_article.category.add(some_category)
