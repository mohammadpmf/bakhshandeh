from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, session


client = MongoClient("localhost", 27017)
db = client['electronics2']
coll = db['devices']
app = Flask(__name__)
app.secret_key = 'your password is incorrect:D'

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        _id = request.form.get('_id')
        p1 = request.form.get('password1')
        p2 = request.form.get('password2')
        if _id in ['', None]:
            error = f"Please fill the ID part!"
            return render_template('register.html', error=error)
        if coll.find_one({'_id': _id}):
            error = f"This ID ({_id}) is already registered! Please choose a different ID."
            return render_template('register.html', error=error)
        if p1!=p2:
            error = "Passwords does not match!"
            return render_template('register.html', error=error)
        new_device = {
            '_id': _id,
            'password': p1
        }
        coll.insert_one(new_device)
        session['_id'] = _id
        return redirect('/')
    return render_template('register.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    status = 200
    if request.method == 'POST':
        _id = request.form.get('_id')
        password = request.form.get('password')
        device = coll.find_one({'_id': _id})
        if device and device['password'] == password:
            session['_id'] = _id
            status = 302
            return redirect('/'), status
        elif device:
            status = 401
            error = "Wrong password!"
            context = {'error': error}
            return render_template('login.html', **context), status
            return render_template('login.html', error="Wrong password!"), status
        else:
            status = 401
            error = f"ID {_id} does not exist!"
            context = {'error': error}
            return render_template('login.html', **context), status
            return render_template('login.html', error=f"ID {_id} does not exist!"), status
    return render_template('login.html')

@app.route('/logout/')
def logout():
    session.clear()
    status = 200
    return render_template('logout.html'), status

@app.route('/')
def home():
    _id = session.get('_id')
    context = {'_id': _id}
    status = 200
    return render_template('home.html', **context), status
    return render_template('home.html', _id=_id), status

app.run(port=5000, debug=True)