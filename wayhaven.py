from flask import Flask, render_template, request, url_for, redirect, session, abort, g, flash, _app_ctx_stack
import time
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from werkzeug import check_password_hash, generate_password_hash

app = Flask(__name__)

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

@app.route('/newStory', methods=['POST', 'GET'])
def new_story():
    if request.method == 'POST':
        return redirect(url_for('view_archives'))
    return render_template('newStory.html')

@app.route('/newChapter', methods=['POST', 'GET'])
def new_chapter():
    if request.method == 'POST':
        return redirect(url_for('view_archives'))
    return render_template('newChapter.html')

@app.route('/aldmoorArchives')
def view_archives():
    return render_template('aldmoorArchives.html', story=story)

@app.route('/account', methods=['POST', 'GET'])
def account_info():
    if request.method == 'POST':
	return redirect(url_for('edit_account_info'))
    return render_template('accountInfo.html')

@app.route('/editAccount', methods=['POST', 'GET'])
def edit_account_info():
    if request.method == 'POST':
	return redirect(url_for('account_info'))
    return render_template('editAccountInfo.html')

if __name__ == '__main__':
    app.run(debug = True)
