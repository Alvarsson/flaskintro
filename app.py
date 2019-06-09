
from flask import Flask, url_for, request, render_template
import time
app = Flask(__name__)

@app.route('/')
def render():
    return render_template('indexpage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            return log_the_user_in(request.form['username'])
    else:
        error = 'Invalid username/password'
    return 'Request method for login no good, %s' % url_for('testHtml')

@app.route('/hello')
def testHtml():
    return "<h1>This is my header</h1>"     
    

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')# show post with the given id
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>') # show subpath
def show_subpath(subpath):
    return 'Subpath %s' % subpath

with app.test_request_context(): #request test vith method POST, can now do something with request until end of with block.I dont do this now THOUGH!!
    
    print(url_for('render'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='Hannah M'))



if __name__ == "__main__":
    app.run("0.0.0.0",3004, debug = True)


