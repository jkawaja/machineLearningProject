import os
from flask import Flask, redirect, url_for, request, render_template, current_app
from forms import RecipeForm, SearchForm
import pandas as pd
from werkzeug.utils import secure_filename

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


if __name__ == '__main__':
    app.run(debug=True)