from flask import Flask, render_template, request
import inter_util as iu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/interpark')
def interpark():
    book_list = iu.inter()
    return render_template('11.interpark.html', book_list=book_list)

if __name__ == '__main__':
    app.run(debug=True)

