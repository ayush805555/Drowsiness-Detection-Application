from flask import Flask, redirect, url_for, render_template, request, session
import os
import mysql.connector
from index import d_dtcn

secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = True

app = Flask(__name__)
app.secret_key = os.urandom(24)

conn = mysql.connector.connect(host="remotemysql.com", user="jmQXLcGlxA", password="vL7QkYx08g", database="jmQXLcGlxA")
cursor = conn.cursor()


@app.route("/")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/index", methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
            return render_template("test1.html")
    else:
        return render_template("index.html")


@app.route("/login_validation", methods=['Post'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
    users = cursor.fetchall()
    if len(users) > 0:
        session['user_id'] = users[0][0]
        return redirect('/index')
    else:
        return redirect('/')


@app.route("/add_user", methods=['Post'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    cursor.execute(
        """INSERT INTO `users` (`user_id`,`name`,`email`,`password`) VALUES (NULL,'{}','{}','{}')""".format(name, email,
                                                                                                            password))
    conn.commit()

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    myuser = cursor.fetchall()
    session['user_id'] = myuser[0][0]
    return redirect('/index')


@app.route("/start", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            d_dtcn()
            return render_template("index.html")
    else:
        return render_template("index.html")


@app.route('/contact', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('contact.html')


if __name__ == "__main__":
    app.run()
