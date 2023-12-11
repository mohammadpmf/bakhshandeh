from flask import Flask, jsonify
from m3 import cpu_percent, ram_percent, ram_usage

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home_page():
    return "Hello"

@app.route("/cpu/", methods=['GET'])
def get_cpu_percentage():
    return cpu_percent()

@app.route("/ram/", methods=['GET'])
def get_ram_percentage():
    return ram_percent()

@app.route("/ram_usage/", methods=['GET'])
def get_ram_usage():
    return ram_usage()

@app.route("/<query>/", methods=['GET'])
def get_news3(query):
    return f'''
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body style="background-color: aqua;">
             Madval messages <br> {query}
        </body>
    </html>
    '''

app.run(port=5000, debug=True)
