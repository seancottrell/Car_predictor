from flask import Flask, redirect,render_template,url_for, request
from flask_material import Material
import pandas as pd
import numpy as np
from sklearn.externals import joblib


app = Flask(__name__)
Material(app)

@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/preview')
def preview():
    df = pd.read_csv("data/iris.csv")
    return render_template("preview.html",df_view = df)

@app.route('/',methods=["POST"])
def analyze():
	if request.method == 'POST':
		petal_length = request.form['petal_length']
		sepal_length = request.form['sepal_length']
		petal_width = request.form['petal_width']
		sepal_width = request.form['sepal_width']
		model_choice = request.form['model_choice']

		# Clean the data by convert from unicode to float
		sample_data = [sepal_length,sepal_width,petal_length,petal_width]
		clean_data = [float(i) for i in sample_data]

		# Reshape the Data as a Sample not Individual Features
		ex1 = np.array(clean_data).reshape(1,-1)


		# Reloading the Model
		if model_choice == 'logitmodel':
		    logit_model = joblib.load('data/logit_model_iris.pkl')
		    result_prediction = logit_model.predict(ex1)
		elif model_choice == 'knnmodel':
			knn_model = joblib.load('data/knn_model_iris.pkl')
			result_prediction = knn_model.predict(ex1)
		elif model_choice == 'svmmodel':
			knn_model = joblib.load('data/svm_model_iris.pkl')
			result_prediction = knn_model.predict(ex1)

	return render_template('index.html', petal_width=petal_width,
		sepal_width=sepal_width,
		sepal_length=sepal_length,
		petal_length=petal_length,
		clean_data=clean_data,
		result_prediction=result_prediction,
		model_selected=model_choice)



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