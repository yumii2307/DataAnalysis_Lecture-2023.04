from flask import Flask, render_template, request
import crawl_util as cu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/interpark2')
def interpark2():
    book_list = cu.interpark()
    return render_template('11.interpark2.html', book_list=book_list)

if __name__ == '__main__':
    app.run(debug=True)

