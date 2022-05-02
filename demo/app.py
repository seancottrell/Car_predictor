from flask import Flask, redirect, render_template, url_for, request, escape
import pandas as pd
import joblib





app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))


# this area is the test code




@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route("/")
def home():
    return render_template("base.html")

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

#-------------------------------------------------------------------------------------#
#--------------------------- ML Model Code -------------------------------------------#
#-------------------------------------------------------------------------------------#


@app.route('/usedCarPredictor')
def usedCarPredictor():
    return render_template("usedCarPredictor.html")

def preprocessDataAndPredict():
    # all inputs stored in an array
    data = [year, manufacturer, condition, cylinders, fuel, odometer, transmission, drive, type, paint_color]

    # create a Data Frame
    data = pd.DataFrame({'Make_year': [year], 'Manufacturer': [manufacturer], 'Condition': [condition], 'Cylinders': [cylinders],
                         'Fuel_type': [fuel], 'Mileage': [odometer], 'Transmission_type': [transmission], 'Drivetrain': [drive],
                         'Vehicle_type': [type], 'Paint_color': [paint_color]})

    # open the file
    file = open("final_model.pkl", "rb")

    # load trained model
    trained_model = joblib.load(file)

    # prediction
    prediction = trained_model.predict(data)

    return round(prediction[0], 0)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        # get the data from user
        year = request.form.get('year')
        manufacturer = request.form.get('manufacturer')
        condition = request.form.get('condition')
        cylinders = request.form.get('cylinders')
        fuel = request.form.get('fuel')
        odometer = request.form.get('odometer')
        transmission = request.form.get('transmission')
        drive = request.form.get('drive')
        type = request.form.get('type')
        paint_color = request.form.get('paint_color')

        # call the preprocessDataAndPredict function and pass the inputs from user
        try:
            prediction = preprocessDataAndPredict()
            # pass the prediction to the template
            return render_template('predict.html', prediction=prediction)

        except ValueError:
            return "Please Enter Valid Values"

        pass
    pass


if __name__ == '__main__':
    app.run(debug=True)
#change homepage.html to the html file in your templates folder