from flask import Flask, render_template, request
from waitress import serve
# import mysql.connector as mc
from msq import insertMoney

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def ind():
    return render_template("index.html")

@app.route("/acceptSend")
def send_page():
    return render_template("sendMoney.html")

@app.route("/checkBal")
def all_page():
    return render_template("allBal.html")

@app.route("/transfer")
def tranfer_money():
    sid = int(request.get("userID"))
    rid = int(request.get("receiverID"))
    amt = int(request.get("amount"))
    
    res = insertMoney(sid, rid, amt)
    if (res == 1):
        return render_template("success.html")
    else:
        return render_template("error.html")


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

