from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/sent")
def logic():
    prompt = request.args.get("user_message")
    response = model.generate_content(f"{prompt}")
    output = response.text
    return render_template(
        "index.html",
        outPut = output,
        Prompt = prompt
    )

if __name__ == "__main__":
    app.run(debug=True)

