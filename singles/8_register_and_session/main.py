from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, session


client = MongoClient("localhost", 27017)
db = client['electronics']
coll = db['devices']
app = Flask(__name__)
app.secret_key = 'your password is incorrect:D'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        _id = request.form.get('_id')
        password = request.form.get('password')
        print(_id, password)
        if coll.find_one({'_id': _id}):
            error = "This ID already taken! Please choose a different ID."
            return render_template('register.html', error=error)        
        new_device = {
            '_id': _id,
            'password': password
        }
        coll.insert_one(new_device)
        session['_id'] = _id
        return redirect('/')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        _id = request.form.get('_id')
        password = request.form.get('password')
        device = coll.find_one({'_id': _id})
        if device and device['password'] == password:
            session['_id'] = _id
            return redirect('/')
        else:
            error = "Invalid ID or password."
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/')
def home():
    _id = session.get('_id')
    return render_template('home.html', _id=_id)

app.run(port=5000, debug=True)