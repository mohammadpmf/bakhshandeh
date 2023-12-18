from flask import Flask, request, jsonify
from m5 import cpu_percent, ram_percent, get_ram_usage, get_ram_usage2

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
    status = 200
    if cpu_usage != 0:
        return f"Status Code is: {status}{'<br>'*2}{cpu_percent(cpu_usage)}", status
    elif ram_usage != 0:
        return f"Status Code is: {status}{'<br>'*2}{ram_percent(ram_usage)}", status
    elif ram_used != 0:
        return f"Status Code is: {status}{'<br>'*2}{get_ram_usage(ram_used, ram_free)}", status
    elif ram_free != 0:
        total_ram = ram_usage+ram_free
        return f"Status Code is: {status}{'<br>'*2}{get_ram_usage2(ram_used, ram_free, total_ram)}", status
    status = 404
    return f"Status Code is: {status}{'<br>'*2}<h1>Page Not Found</h1>", status

@app.errorhandler(404)
def page_not_found(e):
    return f"<h1>Page Totally Not Found</h1>", 404

app.run(port=5000, debug=True)
