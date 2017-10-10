from flask import Flask, render_template, redirect, flash, request, session

app = Flask(__name__)
app.secret_key = "ThisistheSecretKey3"

import datetime
import re

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    fname = request.form['fname']
    lname = request.form['lname']
    pword = request.form['pass']
    cpword = request.form['confirm-pass']

    if len(fname) < 1:
        flash('Please enter your name!')

    if not NAME_REGEX.match(fname):
        print fname
        flash('Please only use letters to spell your first name.')

    if len(lname) < 1:
        print lname
        flash('Please enter your last name!')

    if not NAME_REGEX.match(lname):
        flash('Please only use letters to spell your last name.')

    if len(pword) < 6:
        flash('Password must be at least 6 characters')

    if pword != cpword:
        flash('Passwords do not match')

    else:
        flash('Success! Thanks for registering!')
        session['fname'] = fname
    return redirect('/')


app.run(debug=True)
