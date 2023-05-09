from flask import Flask, render_template, request, redirect
from weather_util import get_weather, get_weather_by_coord
import crawl_util as cu
import genie_util as gu
import siksin_util as su
import map_util as mu
import image_util as iu
import os, random
from datetime import datetime

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    global quote, quotes           # quote, quotes 변수를 전역 변수로 만들어 줌
    global addr
    filename = os.path.join(app.static_folder, 'data/QuoteEnVer.txt')
    with open(filename, encoding='utf-8') as f:
        quotes = f.readlines()
    quote = random.sample(quotes, 1)[0]
    addr = '수원시 장안구'

@app.route('/change_quote')
def change_quote():
    global quote
    quote = random.sample(quotes, 1)[0]
    return quote

@app.route('/change_addr')
def change_addr():
    global addr
    addr = request.args.get('addr')
    return addr

@app.route('/weather')
def weather():
    addr = request.values['addr']
    lat, lng = mu.get_coord(addr + '청')
    html = get_weather_by_coord(app, lat, lng)
    return html

@app.route('/change_profile', methods=['POST'])
def change_profile():
    file_image = request.files['image']
    filename = os.path.join(app.static_folder, f'upload/{file_image.filename}')
    print(filename)
    file_image.save(filename)
    mtime = iu.change_profile(app, filename)
    return str(mtime)

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'api':0, 'cr':0, 'ai':0, 'sc':0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app),
                           quote=quote, addr=addr)

@app.route('/user')
def user():
    menu = {'ho':0, 'us':1, 'api':0, 'cr':0, 'ai':0, 'sc':0}
    return render_template('prototype/user.html', menu=menu, weather=get_weather(app),
                           quote=quote, addr=addr)

@app.route('/interpark')
def interpark():
    menu = {'ho':0, 'us':0, 'api':0, 'cr':1, 'ai':0, 'sc':0}
    book_list = cu.interpark()
    return render_template('prototype/interpark.html', menu=menu, weather=get_weather(app),
                           book_list=book_list, quote=quote, addr=addr)

@app.route('/genie')
def genie():
    menu = {'ho':0, 'us':0, 'api':0, 'cr':1, 'ai':0, 'sc':0}
    music_list = gu.genie()
    now = datetime.now()
    ymd = now.strftime('%Y-%m-%d')
    hh = now.strftime('%H')
    return render_template('prototype/genie.html', menu=menu, weather=get_weather(app),
                           music_list=music_list, quote=quote, addr=addr, ymd=ymd, hh=hh)

@app.route('/siksin', methods=['GET', 'POST'])
def siksin():
    if request.method == 'GET':
        menu = {'ho':0, 'us':0, 'api':0, 'cr':1, 'ai':0, 'sc':0}
        return render_template('prototype/siksin.html', menu=menu, weather=get_weather(app),
                               quote=quote, addr=addr)
    else:
        place = request.form['place']
        menu = {'ho':0, 'us':0, 'api':0, 'cr':1, 'ai':0, 'sc':0}
        food_list = su.siksin(place)
        return render_template('prototype/siksin.html', menu=menu, weather=get_weather(app),
                               food_list=food_list, quote=quote, addr=addr)

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'api':0, 'cr':0, 'ai':0, 'sc':1}
    return render_template('prototype/schedule.html', menu=menu, weather=get_weather(app),
                           quote=quote, addr=addr)

if __name__ == '__main__':
    app.run(debug=True)