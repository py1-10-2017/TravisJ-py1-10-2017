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
    errors = []

    if len(fname) < 1:
        errors.append('Please enter your name!')

    if not NAME_REGEX.match(fname):
        print fname
        errors.append('Please only use letters to spell your first name.')

    if len(lname) < 1:
        print lname
        errors.append('Please enter your last name!')

    if not NAME_REGEX.match(lname):
        errors.append('Please only use letters to spell your last name.')

    if len(pword) < 6:
        errors.append('Password must be at least 6 characters')

    if pword != cpword:
        errors.append('Passwords do not match')

    if len(errors) > 0:
        for error in errors:
            flash(error)
    else:
        flash('Success! Thanks for registering!')
        session['fname'] = fname
        return redirect('/registered')

    return redirect('/')


@app.route('/registered')
def registered():
    return render_template('success.html', fname=session['fname'])


app.run(debug=True)
