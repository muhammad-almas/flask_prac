#import the Flask class and create an instance of it
from flask import Flask, render_template

app = Flask(__name__)

# test post dictionary
posts = {
    1: {'title': 'Introduction to Flask', 'content': 'Flask is a lightweight WSGI web application framework...'},
    2: {'title': 'Understanding Routes in Flask', 'content': 'Routes are a fundamental concept in Flask...'}
}

#define homepage route and index() view function
# Pass the required route to the decorator
@app.route('/')
def index():
    return render_template('index.html')

# testing post route
@app.route('/post/1')
def show_post():
    post = posts[1]
    return f"<h1>{post['title']}</h1><p>{post['content']}</p>"

#run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
