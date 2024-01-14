from flask import Flask, request
from m5 import *

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home_page():
    return "Hello"

@app.route("/receive", methods=['GET'])
def get_info():
    cpu_usage  = request.args.get('cpu_usage', 0)
    ram_usage  = request.args.get('ram_usage', 0)
    ram_used  = request.args.get('ram_used', 0)
    ram_free  = request.args.get('ram_free', 0)
    ram_used2  = request.args.get('ram_used2', 0)
    ram_free2  = request.args.get('ram_free2', 0)
    status = 200
    if cpu_usage != 0:
        return f"Status Code is: {status}{'<br>'*2}{cpu_percent(cpu_usage)}", status
    elif ram_usage != 0:
        return f"Status Code is: {status}{'<br>'*2}{ram_percent(ram_usage)}", status
    elif ram_used != 0 and ram_free != 0:
        return f"Status Code is: {status}{'<br>'*2}{get_ram_usage(ram_used, ram_free)}", status
    elif ram_used2 != 0 and ram_free2 != 0:
        return f"Status Code is: {status}{'<br>'*2}{get_ram_usage2(ram_used2, ram_free2)}", status
    status = 404
    return f"Status Code is: {status}{'<br>'*2}<h1>Query params are not right.</h1>", status

@app.errorhandler(404)
def page_not_found(e):
    return f"<center><h1>Page Not Found</h1><br><p>{e}</p></center>", 404

app.run(port=5000, debug=True)
