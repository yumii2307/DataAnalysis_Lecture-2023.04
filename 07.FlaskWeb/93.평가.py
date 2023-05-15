from flask import Flask, render_template, request
import test_util as tu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/melon')
def melon():
    music_list = tu.melon()
    return render_template('93.평가.html', music_list=music_list)

@app.route('/youtube_ranking', methods=['GET', 'POST'])
def YT_ranking():
    if request.method == 'GET':
        return render_template('94.spinner.html')
    else:
        ranking_list = tu.YT_ranking()
        return render_template('94.평가.html', ranking_list=ranking_list)

@app.route('/re_youtube_ranking')
def re_YT_ranking():
    ranking_list = tu.re_YT_ranking()
    return render_template('94.평가.html', ranking_list=ranking_list)

@app.route('/top20')
def YT_ranking_Top20():
    ranking_list = tu.YT_ranking_Top20()
    return render_template('95.평가.html', ranking_list=ranking_list)

@app.route('/top10')
def YT_ranking_Top10():
    ranking_list = tu.YT_ranking_Top10()
    return render_template('96.평가.html', ranking_list=ranking_list)

if __name__ == '__main__':
    app.run(debug=True)
    
