from flask import Flask
from m4 import *

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

app.run(port=5000, debug=True)
