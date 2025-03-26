from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/hello/")
@app.route("/hello/<name>")
def hello_world(name=None):
    return render_template('hello.html', person=name)

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')
