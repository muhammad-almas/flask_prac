#import the Flask class and create an instance of it
from flask import Flask, render_template, request, redirect, url_for
from forms import HealthDataForm # import HealthDataFrom class from forms.py
from flask_sqlalchemy import SQLAlchemy

# import db_uri from db_uri.py file.
import os, sys
parent_dir = os.path.dirname(os.path.abspath(__file__)) # path for current directory
parent_dir = os.path.dirname(parent_dir) # path for parent directory
sys.path.append(parent_dir) # add path to sys.path
from db_uri import db_uri # import db_uri


app = Flask(__name__)

# required for form handling in flask
app.secret_key = 'supersecretkey'

# setup Sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class HealthData(db.Model):
    __tablename__ = 'health_data'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    exercise = db.Column(db.Integer, nullable=False)
    meditation = db.Column(db.Integer, nullable=False)
    sleep = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<HealthData {self.id}>'


#define homepage route and index() view function
# Pass the required route to the decorator
@app.route('/')
def index():
    return render_template('index.html')

# route for form. it supports both get and post. it uses request, recirect and url_for (imported above)
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = HealthDataForm() # initialize form class
    if request.method == 'POST' and form.validate_on_submit():
        # Process form data here
        # Create a new health data entry
        new_data = HealthData(
            date=form.date.data,
            exercise = form.exercise.data,
            meditation = form.meditation.data,
            sleep = form.sleep.data
        )
        # Add the new data to the database
        db.session.add(new_data)
        db.session.commit()
        # Redirect to the dashboard
        return redirect(url_for('dashboard'))
    return render_template('form.html', form=form) # pass forms variable to forms template

# route for dashboard
@app.route('/dashboard')
def dashboard():
    # Retrieve all health data from the database
    all_data = HealthData.query.all()
    # Prepare data for charts
    dates = [data.date.strftime("%Y-%m-%d") for data in all_data]
    exercise_data = [data.exercise for data in all_data]
    meditation_data = [data.meditation for data in all_data]
    sleep_data = [data.sleep for data in all_data]

    return render_template('dashboard.html', dates=dates, exercise_data=exercise_data, meditation_data=meditation_data, sleep_data=sleep_data)



#run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
