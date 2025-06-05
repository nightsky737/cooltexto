from flask import *
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")#Route binds the function to a url So visiting ~/n1ghtsky will run this code and say hello, nightsky
def hello(name):
    return f"Hello, {escape(name)}!" #Escapes it so that u cant put ur name as malicious code and have it get runned
#Note about routing: Folders will have a / after (so /stuff/ is a folder, and /stuff will redirect to /stuff/ while /stuff is a file and /stuff/ is not found  )
#These urls are unique!

@app.route('/<int:post_id>') #now runs if its an integer after it.
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context(): #Tests as if we had made a get request w/ this
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))