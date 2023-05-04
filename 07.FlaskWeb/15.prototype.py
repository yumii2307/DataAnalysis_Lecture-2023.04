from flask import Flask, render_template, request
from weather_util import get_weather
import crawl_util as cu
import genie_util as gu
import siksin_util as su

app = Flask(__name__)

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'api':0, 'cr':0, 'ai':0, 'sc':0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app))

@app.route('/user')
def user():
    menu = {'ho':0, 'us':1, 'api':0, 'cr':0, 'ai':0, 'sc':0}
    return render_template('prototype/user.html', menu=menu, weather=get_weather(app))

@app.route('/interpark')
def interpark():
    menu = {'ho':0, 'us':0, 'api':0, 'cr':1, 'ai':0, 'sc':0}
    book_list = cu.interpark()
    return render_template('prototype/interpark.html', menu=menu, weather=get_weather(app), book_list=book_list)

@app.route('/genie')
def genie():
    menu = {'ho':0, 'us':0, 'api':0, 'cr':1, 'ai':0, 'sc':0}
    music_list = gu.genie()
    return render_template('prototype/genie.html', menu=menu, weather=get_weather(app), music_list=music_list)

@app.route('/siksin')
def siksin():
    menu = {'ho':0, 'us':0, 'api':0, 'cr':1, 'ai':0, 'sc':0}
    food_list = su.siksin()
    return render_template('prototype/siksin.html', menu=menu, weather=get_weather(app), food_list=food_list)

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'api':0, 'cr':0, 'ai':0, 'sc':1}
    return render_template('prototype/schedule.html', menu=menu, weather=get_weather(app))

if __name__ == '__main__':
    app.run(debug=True)