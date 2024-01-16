from flask import Flask, request, render_template
from m7 import ComputerInfo
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.get_database('electronics1')
coll = db.get_collection('devices')
coll.create_index([('device_id', 1)], unique=True)


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home_page():
    return render_template("home.html")

@app.route("/receive", methods=['GET'])
def get_info():
    status = 200 # Everything is ok
    errors = []
    device_id = request.args.get('device_id', None)
    if device_id == None:
        errors.append("You must Enter a Device ID!")
        status = 405 # not allowed because of web server
    else:
        try:
            result = coll.find_one({'device_id': device_id})
            print(result)
            print(result['device_id'])
        except:
            status = 401 # unauthorized
            errors.append(f"The device with device id '{device_id}' is not Registered in db")
    cpu_usage = request.args.get('cpu_usage', 0)
    try:
        cpu_usage = float(cpu_usage)
        if cpu_usage>100 or cpu_usage<0:
            errors.append("cpu_usage must be in range 0 and 100")
    except:
        status = 400 # Bad Request
        return f"Status Code is: {status}{'<br>'*2}<h1>cpu_usage must be a number.</h1>", status
    ram_usage = request.args.get('ram_usage', 0)
    try:
        ram_usage = float(ram_usage)
        if ram_usage>100 or ram_usage<0:
            errors.append("ram_usage must be in range 0 and 100")
    except:
        status = 400 # Bad Request
        return f"Status Code is: {status}{'<br>'*2}<h1>ram_usage must be a number.</h1>", status
    ram_used = request.args.get('ram_used', 0)
    try:
        ram_used = float(ram_used)
        if ram_used<0:
            errors.append("ram_used must be greater than 0")
    except:
        status = 400 # Bad Request
        return f"Status Code is: {status}{'<br>'*2}<h1>ram_used must be a number.</h1>", status
    ram_free = request.args.get('ram_free', 0)
    try:
        ram_free = float(ram_free)
        if ram_free<0:
            errors.append("ram_free must be greater than 0")
    except:
        status = 400 # Bad Request
        return f"Status Code is: {status}{'<br>'*2}<h1>ram_free must be a number.</h1>", status
    ram_used2 = request.args.get('ram_used2', 0)
    try:
        ram_used2 = float(ram_used2)
        if ram_used2<0:
            errors.append("ram_used2 must be greater than 0")
    except:
        status = 400 # Bad Request
        return f"Status Code is: {status}{'<br>'*2}<h1>ram_used2 must be a number.</h1>", status
    ram_free2  = request.args.get('ram_free2', 0)
    try:
        ram_free2 = float(ram_free2)
        if ram_free2<0:
            errors.append("ram_free2 must be greater than 0")
    except:
        status = 400 # Bad Request
        return f"Status Code is: {status}{'<br>'*2}<h1>ram_free2 must be a number.</h1>", status
    this_pc = ComputerInfo(cpu_usage, ram_usage, ram_used, ram_free, ram_used2, ram_free2)
    if len(errors)!=0:
        context = { 'errors': errors }
        return render_template("home.html", **context), status
    if cpu_usage != 0:
        return f"Status Code is: {status}{'<br>'*2}{this_pc.get_cpu_percent()}", status
    elif ram_usage != 0:
        return f"Status Code is: {status}{'<br>'*2}{this_pc.get_ram_percent()}", status
    elif ram_used != 0 and ram_free != 0:
        return f"Status Code is: {status}{'<br>'*2}{this_pc.get_ram_usage()}", status
    elif ram_used2 != 0 and ram_free2 != 0:
        return f"Status Code is: {status}{'<br>'*2}{this_pc.get_ram_usage2()}", status
    status = 400 # Bad Request
    return f"Status Code is: {status}{'<br>'*2}<h1>Query params are not right.</h1>", status

@app.errorhandler(404)
def page_not_found(e):
    return f"<center><h1>Page Not Found</h1><br><p>{e}</p></center>", 404


@app.route('/register/', methods=["GET"])
def register():
    return render_template("sign_up.html")


@app.route('/register/', methods=["POST"])
def register2():
    device_id=request.form.get("device_id", None)
    print(device_id)
    if len(device_id)==0:
        context = {'error': "Device Must have an ID!"}
        return render_template("sign_up.html", **context)
    try:
        coll.insert_one({"device_id": device_id})
        return render_template("success.html")
    except:
        context = {'error': f"Device with ID '{device_id}' already exists!"}
        return render_template("sign_up.html", **context)


app.run(port=5007, debug=True)