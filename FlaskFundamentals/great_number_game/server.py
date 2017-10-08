from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)


app.secret_key = 'lskdjf;lajfj'

import random


@app.route('/')
def main():
    if 'winning_number' not in session:
        session['winning_number'] = random.randrange(0, 101)
        #session['response'] = ''
        print session['winning_number'], "- is the winning number"

    return render_template('index.html', response=session['response'])


@app.route('/guess', methods=['POST'])
def guess():
    guess = request.form['guess']
    winning_number = session['winning_number']

    if int(guess) > int(winning_number):
        print "Too high."
        session['response'] = str(guess) + ' - Too high!'
        return redirect('/')
    elif int(guess) < int(winning_number):
        print "Too low."
        session['response'] = str(guess) + ' - Too low!'
        return redirect('/')
    else:
        print winning_number, " is correct! You win!"
        session['response'] = str(winning_number) + " - You win!"
        session.pop('winning_number')
        return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():

    return redirect('/')


app.run(debug=True)
