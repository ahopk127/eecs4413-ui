from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/auctions")
def auctions():
    return render_template('auctions.html')

@app.route("/auctions/forward/<auctionId>")
def forward(auctionId: int):
    return render_template('bid_forward.html', auctionId=auctionId)

@app.route("/auctions/dutch/<auctionId>")
def dutch(auctionId: int):
    return render_template('bid_dutch.html', auctionId=auctionId)
