from decimal import Decimal
import decimal
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange

class CarInfoForm(FlaskForm):
    carCylinders = IntegerField("Cylinders:", default=3, validators=[DataRequired(), NumberRange(min=3, max=8)],
                                render_kw={"title": "Cylinders must be between 3 and 8."})
    carHorsepower = DecimalField("Horsepower:", default=Decimal(40), places=2, rounding=decimal.ROUND_UP,
                                 validators=[DataRequired(), NumberRange(min=40, max=250)],
                                 render_kw={"title": "Horsepower must be between 40 and 250."})
    carWeight = IntegerField("Weight:", default=1600, validators=[DataRequired(), NumberRange(min=1600, max=5500)],
                             render_kw={"title": "Weight must be between 1600 and 5500."})
    carYear = IntegerField("Year:", default=1965, validators=[DataRequired(), NumberRange(min=1965, max=1987)],
                           render_kw={"title": "Year must be between 1965 and 1987."})
    carOrigin = SelectField("Origin:", choices=[("USA", "USA"), ("Japan", "Japan"),  ("Europe", "Europe")],
                            validators=[DataRequired()])
    submit = SubmitField("Submit")


class PersonInfoForm(FlaskForm):
    personGlucose = IntegerField("Glucose:", validators=[DataRequired(), NumberRange(min=30, max=200)],
                                 render_kw={"title": "Glucose must be between 30 and 200"},
                                 default=30)
    personBMI = DecimalField("BMI:", validators=[DataRequired(), NumberRange(min=10, max=80)],
                             render_kw={"title": "BMI must be between 10 and 80"},
                             default=Decimal(10))
    personAge = IntegerField("Age:", validators=[DataRequired(), NumberRange(min=20, max=100)],
                             render_kw={"title": "Age must be between 20 and 100"},
                             default=20)
    submit = SubmitField("Submit")
