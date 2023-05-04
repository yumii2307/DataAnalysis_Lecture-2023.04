import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

def siksin(place):
    base_url = 'https://www.siksinhot.com/search'
    url = f'{base_url}?keywords={quote(place)}'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    lis = soup.select('.localFood_list > li')
    line = []
    for li in lis:
        img = li.find('img')['src']
        title = li.select_one('.textBox > h2').get_text()
        score = li.select_one('.textBox > .score').get_text()
        atags = li.select('.cate > a')
        location = atags[0].get_text()
        menu = atags[1].get_text()
        line.append({'img': img, 'title': title, 'score': score, 'location': location, 'menu': menu})
    
    return line