from flask import Flask, render_template, redirect, flash, request, session

app = Flask(__name__)
app.secret_key = "ThisistheSecretKey2"

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

    elif not NAME_REGEX.match(fname):
        print fname
        flash('Please only use letters to spell your first name.')

    elif len(lname) < 1:
        print lname
        flash('Please enter your last name!')

    elif not NAME_REGEX.match(lname):
        flash('Please only use letters to spell your last name.')

    elif len(pword) < 6:
        flash('Password must be at least 6 characters')

    elif pword != cpword:
        flash('Passwords do not match')

    else:
        flash('Success! Thanks for registering!')
        session['fname'] = fname
    #     return render_template('success.html', fname=fname, lname=lname)
    return redirect('/registered')


@app.route('/registered')
def registered():
    return render_template('success.html', fname=session['fname'])


app.run(debug=True)
