from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/about")
def projectwriteup():
    return render_template("project_writeup.html")

@app.route("/Alec_Harrod")
def alec():
    return render_template("resume_alec.html")

@app.route("/Roshane_Bent")
def roshane():
    return render_template("resume_roshane.html")

@app.route("/Isaac_Matsko")
def isaac():
    return render_template("resume_isaac.html")

@app.route("/Sean_Cottrell")
def sean():
    return render_template("resume_sean.html")


if __name__ == '__main__':
    app.run(debud=True)
#change homepage.html to the html file in your templates folder