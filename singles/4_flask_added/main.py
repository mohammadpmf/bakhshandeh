from flask import Flask
from m4 import cpu_percent, ram_percent, ram_usage

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

# @app.route("/ram/<query>/", methods=['POST']) # In this code, output is "Method not allowed in html"
# @app.route("/ram/<query>/") # works
@app.route("/ram/<query>/", methods=['GET'])
def my_test(query):
    return f'''
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body style="background-color: aqua;">
             Mohammad messages <br> {query}
        </body>
    </html>
    '''

app.run(port=5000, debug=True)
