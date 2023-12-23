from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)


db.init_app(app)


with app.app_context():
    db.create_all()


@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/logout")
def logout():
    logout_user()
    return render_template("logout.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form.get("username")).first()
        if user:
            if user.password == request.form.get("password"):
                login_user(user)
                return redirect(url_for("home"))
            context = {'error': 'Wrong Password'}
            return render_template("login.html", **context)
        context = {'error': 'Username does not exists!'}
        return render_template("login.html", **context)
    return render_template("login.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        password1=request.form.get("password1")
        password2=request.form.get("password2")
        if password1!=password2:
            context = {'errors': ["Passwords Does Not Match"]}
            # میخواستم حالت های مختلف رو در نظر بگیرم اما موقع کد نویسی خیلی رو اعصابه فقط همین رو چک کردم.
            # اگه گروهی قوی بودن میشه اضافه کرد. حتی چک کردم میشه پسوورد رو هش هم کرد. و از تابع های آماده استفاده کرد.
            # اما باز همون مشکل پیش میاد که بچه ها میگن از کجا باید بدونیم این رو باید ایمپورت کرد.
            # گفتم هدف این بود که از فلسک استفاده کنیم که ساده تر باشه. وگرنه مال جنگو که ساده تر خودش درست میکنه و هش هم میکنه و رابط گرافیکی آماده هم داره.
            # به هر حال با نام errors فرستادم که for هم گفته بشه اون ور.
            return render_template("sign_up.html", **context)
        user = Users(username=request.form.get("username"), password=password1)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("sign_up.html")


if __name__ == "__main__":
    app.run()
