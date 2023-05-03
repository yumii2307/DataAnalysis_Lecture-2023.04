import requests, os
from bs4 import BeautifulSoup

def inter():
    url = 'http://book.interpark.com/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    lis = soup.select('.rankBestContentList > ol > li')
    li = lis[0]
    lines = []
    for li in lis:
        rank_data = li.select('.rankBtn_ctrl')
        if len(rank_data) == 1:
            rank = int(rank_data[0]['class'][-1][-1])
        else:
            rank = int(rank_data[0]['class'][-1][-1] + rank_data[1]['class'][-1][-1])
        image = li.select_one('img')['src']
        title = li.select_one('.itemName').get_text().strip()
        href = li.select_one('.coverImage').find('a')['href']
        author = li.select_one('.author').get_text().strip()
        company = li.select_one('.company').get_text().strip()
        price = li.select_one('.price > em').get_text().strip()   
        lines.append({'순위':rank, '이미지':image, '타이틀':title, 'href':'http://book.interpark.com'+href,
                      '저자':author, '출판사':company, '가격':price})

    return lines