import os
from flask import Flask, redirect, url_for, request, render_template, current_app
from forms import CarInfoForm
from datetime import datetime
import numpy as np
import warnings
from joblib import load


import pandas as pd
from werkzeug.utils import secure_filename

warnings.filterwarnings("ignore")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asfhdasfhbakwjbkfefr7y57y47rjbfkabzfcbhafbka'
app.config['SUBMITTED_DATA'] = os.path.join('static', 'data_dir','')
app.config['SUBMITTED_IMG'] = os.path.join('static', 'image_dir','')

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
            car_dict = {"cylinders": car_cylinders, "horsepower": car_horsepower, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 0, "origin_usa": 1}
        elif car_origin == "Japan":
            car_dict = {"cylinders": car_cylinders, "horsepower": car_horsepower, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 1, "origin_usa": 0}
        else:
            car_dict = {"cylinders": car_cylinders, "horsepower": car_horsepower, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 0, "origin_usa": 0}

        input_array = np.array(list(car_dict.values())).reshape(1, -1)


        mpg_model = load("mpg_model.joblib")
        mpg_final = mpg_model.predict(input_array)

        return render_template("index.html")
    else:
        return render_template("add_car_info.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)