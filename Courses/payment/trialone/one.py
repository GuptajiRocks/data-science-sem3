from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def ind():
    return render_template("index.html")

@app.route("/acceptsend")
def send_page():
    return render_template("sendMoney.html")

@app.route("/checkBal")
def all_page():
    return render_template("allBal.html")


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

