import requests, time
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns

def melon():
    lines = []
    test = pd.read_csv('static/data/멜론_2023051215.csv').to_dict()
    for i in range(len(test['rank'])): 
        lines.append({'rank': test['rank'][i], 'image': test['image'][i],
                      'title': test['title'][i], 'artist': test['artist'][i], 'album': test['album'][i]})

    return lines

import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')

def convert(s):
    s = s.replace('억','').replace('개','').replace(',','').replace('만','0000')
    return int(s)

def YT_ranking():
    lines = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome('C:/Users/YONSAI/Downloads/chromedriver', options=options)
    for page in range(1, 11):
        url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=' + str(page)
        driver.get(url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        trs = soup.select('.aos-init')
        for tr in trs:
            rank = tr.select_one('.rank').get_text().strip()
            category = tr.select_one('.category').get_text().strip()[1:-1]
            channel = tr.select_one('.subject > h1 > a').get_text().strip()
            구독자수 = convert(tr.select_one('.subscriber_cnt').get_text().strip())
            view = tr.select_one('.view_cnt').get_text().strip()
            video = tr.select_one('.video_cnt').get_text().strip()
            lines.append({'rank':rank, 'category':category, 'channel':channel,
                        '구독자수':구독자수, 'view':view, 'video':video})
            
    df = pd.DataFrame(lines)
    df.to_csv('static/data/youtube_ranking.csv', index=False)
            
    return lines

def re_YT_ranking():
    df = pd.read_csv('static/data/youtube_ranking.csv').to_dict()
    lines = []
    for i in range(len(df['rank'])): 
        lines.append({'rank': df['rank'][i], 'category': df['category'][i], 'channel': df['channel'][i],
                      '구독자수': df['구독자수'][i], 'view': df['view'][i], 'video': df['video'][i]})
        
    return lines

def YT_ranking_Top20():
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    df = pd.read_csv('static/data/youtube_ranking.csv')
    df1 = df.sort_values(by='구독자수', ascending=False)

    plt.figure(figsize=(12,8))
    sns.barplot(y='channel', x='구독자수', data=df1.head(20))
    plt.title('구독자수 Top 20 채널')
    plt.savefig('static/img/top20_subscriber.png')

def YT_ranking_Top10():
    df = pd.read_csv('static/data/youtube_ranking.csv')
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    df3 = df.category.value_counts().to_frame()

    plt.figure(figsize=(12,5))
    sns.barplot(y=df3.index[:10], x='count', data=df3.head(10))
    plt.title('카테고리별 채널수 Top 10')
    plt.savefig('static/img/top10_category.png')