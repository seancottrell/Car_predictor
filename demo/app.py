from flask import Flask, redirect,render_template,url_for


app = Flask(__name__)

@app.route('/home')
def homepage():
    return render_template("home.html")


@app.route("/")
def home():
    return render_template("index.html", content="Testing")

@app.route("/admin")
def admin():
    return redirect(url_for("main", name="Admin!"))

@app.route('/about')
def projectwriteup():
    return render_template("project_writeup.html")

@app.route('/alec')
def alec():
    return render_template("resume_alec.html")

@app.route('/roshane')
def roshane():
    return render_template("resume_shane.html")

@app.route('/isaac')
def isaac():
    return render_template("resume_isaac.html")

@app.route('/sean')
def sean():
    return render_template("resume_sean.html")


if __name__ == '__main__':
    app.run(debug=True)
#change homepage.html to the html file in your templates folder