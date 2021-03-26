from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/")
def start():
    return "This is the acutal Flask which shuold open in 127.0.0 from ngrok"
