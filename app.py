#import the Flask class and create an instance of it
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#define homepage route and index() view function
# Pass the required route to the decorator
@app.route('/')
def index():
    return render_template('index.html')

# route for form. it supports both get and post. it uses request, recirect and url_for (imported above)
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Process form data here
        return redirect(url_for('dashboard'))
    return render_template('form.html')

# route for dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# required for form handling in flask
app.secret_key = 'supersecretkey'

# import MyForm class from test_form.py
from test_form import MyForm
# create route for test_form template
@app.route('/test_form', methods=['GET', 'POST'])
def test_form():
    form = MyForm() # initialize class
    if request.method == 'POST':
        return f"Hello, {form.username.data}!"
    return render_template('test_form.html', form=form)

#run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
