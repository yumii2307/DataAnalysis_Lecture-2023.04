import requests
from bs4 import BeautifulSoup

def genie():
    url = 'https://www.genie.co.kr/chart/top200'
    result = requests.get(url)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, 'html.parser')
    trs = soup.select('tr.list')
    tr = trs[0]
    line = []
    for tr in trs:
        rank = tr.select_one('.number').get_text().split('\n')[0].strip()
        img = 'https:' + tr.select_one('.cover').find('img')['src']
        title = tr.select_one('.info > .title.ellipsis').get_text().split('\n')[-1].strip()
        artist = tr.select_one('.info > .artist.ellipsis').get_text().strip()
        album = tr.select_one('.info > .albumtitle.ellipsis').get_text()
        line.append({'rank': rank, 'img': img, 'title': title, 'artist': artist, 'album': album})

    return line