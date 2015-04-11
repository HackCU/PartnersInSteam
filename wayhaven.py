from flask import Flask, render_template, request, url_for, redirect, session, abort, g, flash
'''import time
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash'''

app = Flask(__name__)

story = ""

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/logout')
def logout():
    flash('You were logged out')
    #session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/newChapter', methods=['POST', 'GET'])
def new_chapter():
    global story
    if request.method == 'POST':
        story = request.form['contents']
        return redirect(url_for('view_story'))
    return render_template('newChapter.html')

@app.route('/story')
def view_story():
    return render_template('story.html', story=story)

if __name__ == '__main__':
    app.run(debug = True)
