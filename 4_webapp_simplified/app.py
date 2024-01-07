from flask import Flask, jsonify
import services

app = Flask(__name__)

@app.route("/")
def get_news():
    return "no news is good news"

@app.route("/mohammad/")
def get_news2():
    return "Mohammad message"

@app.route("/mohammad/<test>/")
def get_news3(test):
    return f'''
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body style="background-color: aqua;">
             Mohammad messages <br> {test}
        </body>
    </html>
    '''

@app.route('/news/all/', methods=['GET'])
def a1():
    news = services.news_list()
    return jsonify(news)


@app.route('/news/<news_id>/', methods=['GET'])
def a2(news_id: str):
    n = services.news_details(news_id)
    return jsonify(n)


@app.route('/search/<query>/', methods=['GET'])
def a3(query:str):
    news = services.news_search(query)
    return jsonify(news)


@app.route('/update/', methods=['GET'])
def a4():
    data = services.update_collection()
    return jsonify(data)


app.run(port=5000, debug=True)
