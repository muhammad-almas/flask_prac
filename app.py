#import the Flask class and create an instance of it
from flask import Flask, render_template, request, redirect, url_for
from forms import HealthDataForm # import HealthDataFrom class from forms.py

app = Flask(__name__)

# required for form handling in flask
app.secret_key = 'supersecretkey'

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
        date=form.date.data
        exercise = form.exercise.data
        meditation = form.meditation.data
        sleep = form.sleep.data
        # Redirect to the dashboard
        return redirect(url_for('dashboard'))
    return render_template('form.html', form=form) # pass forms variable to forms template

# route for dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


#run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
