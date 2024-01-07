from flask import Flask

app = Flask(__name__)

@app.route("/")
def alaki2():
    return "Welcome to my site"

@app.route("/mohammad/")
def alaki():
    return "Welcome from mohammad"

@app.route("/mohammad/<int:name>/")
def alaki3(name):
    return f"Welcome from {name}"
# دقت کنید که اسپیس اضافه ارور میده. یعنی این شکلی مشکل داره اگه بعد از دو نقطه اینت اسپیس بذارید.
# @app.route("/mohammad/<int: name>/")
# def alaki33333(name):
#     return f"Welcome from {name}"

@app.route("/<n1>/<n2>/<n3>/")
def alaki4(n1, n2, n3):
    return f"Welcome from {n1} {n2} {n3}"

app.run(port=5000, debug=True)