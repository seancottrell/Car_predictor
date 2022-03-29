from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

#change homepage.html to the html file in your templates folder