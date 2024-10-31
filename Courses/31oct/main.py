from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route("/")
def ind():
    return render_template("index.html")

@app.route("/send")
def sendmon():
    return render_template("sent.html")



if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
