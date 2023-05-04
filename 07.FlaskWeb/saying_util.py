import requests, time, random
from urllib.parse import quote
from bs4 import BeautifulSoup
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')

def saying():
    base_url = 'https://en.dict.naver.com/'
    url = f'{base_url}#/search?range=example&shouldSearchVlive=false&query={quote("명언")}&autoConvert='

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')   # 화면없이 실행
    options.add_argument('--no-sandbox')
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome('C:/Users/YONSAI/Downloads/chromedriver', options=options)
    driver.get(url)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    divs = soup.select('.component_example.has-saving-function > .row')
    list_ = []
    for div in divs:
        say = div.select_one('.text').get_text().strip()
        list_.append(say)

    saying = random.choice(list_)

    return saying