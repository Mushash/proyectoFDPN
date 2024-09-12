from flask import Flask, render_template,url_for
from config import config

fdpnApp = Flask("/")
def home():
    return render_template("home.html")

if __name__=="_main_":
    fdpnApp.run(debug=True,port=3300)