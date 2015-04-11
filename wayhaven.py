from flask import Flask, render_template, request, url_for, redirect, session, abort, flash, _app_ctx_stack
import time
from hashlib import md5
from datetime import datetime
from werkzeug import check_password_hash, generate_password_hash

from app import app
from db import db

#from sqlalchemy import Table, Column, Integer, String
#from sqlalchemy.orm import mapper
#from yourapplication.database import metadata, db_session

''' DATABASE '''

''' ROUTES '''

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        user_email = request.form['email']
        password1 = request.form['password']
        password2 = request.form['password2']
        if password1 != password2:
            return render_template('register.html', message="Passwords do not match")
        return render_template('register.html')
    else:
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
    return render_template('aldmoorArchives.html')

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
    db.create_all()
    app.run(debug = True)
