#import the Flask class and create an instance of it
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#define homepage route and index() view function
# Pass the required route to the decorator
@app.route('/')
def index():
    user = {'username': 'Jhon'}
    items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('index.html', title='Home', user=user, items=items)

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

# route for welcome
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

#run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
