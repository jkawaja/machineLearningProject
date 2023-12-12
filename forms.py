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