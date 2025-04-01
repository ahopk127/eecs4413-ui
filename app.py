from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/resetpass")
def reset_password():
    return render_template('resetPassword.html')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/auctions")
def auctions():
    return render_template('auctions.html')

@app.route("/auctions/sell")
def sell():
    return render_template('sell.html')

@app.route("/auctions/forward/<auctionId>")
def forward(auctionId: int):
    return render_template('bid_forward.html', auctionId=auctionId)

@app.route("/auctions/dutch/<auctionId>")
def dutch(auctionId: int):
    return render_template('bid_dutch.html', auctionId=auctionId)

@app.route("/auctions/done/<auctionId>")
def auction_done(auctionId: int):
    return render_template('auction_ended.html', auctionId=auctionId)

@app.route("/auctions/pay/<auctionId>/")
def pay(auctionId: int):
    expedited = request.args.get('expedited')
    return render_template('pay.html', auctionId=auctionId, expedited=expedited)

@app.route("/auctions/receipt/<auctionId>/")
def receipt(auctionId: int):
    return render_template('receiving.html', auctionId=auctionId)

@app.route("/auctions/setprice/<auctionId>/")
def set_price(auctionId: int):
    return render_template('set_dutch.html', auctionId=auctionId)

@app.route("/styles.css")
def styles() -> Response:
    return Response(render_template('styles.css'), mimetype='text/css')

@app.route("/navcode.js")
def navcode() -> Response:
    return Response(render_template('navcode.js'), mimetype='text/javascript')
