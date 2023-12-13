import os
from flask import Flask, redirect, url_for, request, render_template, current_app
from forms import CarInfoForm, PersonInfoForm
from datetime import datetime
import numpy as np
import warnings
from joblib import load


import pandas as pd
from werkzeug.utils import secure_filename

warnings.filterwarnings("ignore")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asfhdasfhbakwjbkfefr7y57y47rjbfkabzfcbhafbka'

@app.route('/')
def greetings():
    """
    Function to show example instance
    :return:
    """
    return render_template('index.html')

@app.route('/carInfo', methods=['POST', 'GET'])
def get_car_info():
    form = CarInfoForm()
    if form.validate_on_submit():
        car_cylinders = form.carCylinders.data
        car_horsepower = form.carHorsepower.data
        car_weight = form.carWeight.data
        car_year = form.carYear.data
        car_origin = form.carOrigin.data

        if car_origin == "USA":
            car = {"cylinders": car_cylinders, "horsepower": car_horsepower, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 0, "origin_usa": 1}
        elif car_origin == "Japan":
            car = {"cylinders": car_cylinders, "horsepower": car_horsepower, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 1, "origin_usa": 0}
        else:
            car = {"cylinders": car_cylinders, "horsepower": car_horsepower, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 0, "origin_usa": 0}
        inputArray = np.array(list(car.values())).reshape(1, -1)

        mpg_model = load("mpg_model.joblib")
        mpg_final = mpg_model.predict(inputArray)

        return render_template("view_mpg_results.html",
                               car=car,
                               mpg_final=round(mpg_final[0], 2))
    else:
        return render_template("add_car_info.html", form=form)


@app.route('/personInfo', methods=['POST', 'GET'])
def get_person_info():
    form = PersonInfoForm()
    if form.validate_on_submit():
        person_glucose = form.personGlucose.data
        person_bmi = form.personBMI.data
        person_age = form.personAge.data

        person = {"glucose": person_glucose, "bmi": person_bmi, "age": person_age}
        inputArray = np.array(list(person.values())).reshape(1, -1)

        diabetes_model = load("diabetes_model.joblib")
        diabetes_final = diabetes_model.predict(inputArray)

        return render_template("view_diabetes_results.html", person=person,
                               diabetes_final=diabetes_final)

    else:
        return render_template("add_person_info.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)