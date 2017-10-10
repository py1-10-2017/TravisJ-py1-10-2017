from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)


app.secret_key = 'lskdjf;lajf'

import random


@app.route('/')
def main():
    if 'winning_number' not in session:
        session['winning_number'] = random.randrange(0, 101)
        print session['winning_number'], "- is the winning number"

    #session['response'] = "Take a Guess"
    if 'response' not in session and 'winner' not in session:
        print "case 1"
        return render_template('index.html')
    elif 'winner' not in session:
        print "case 2"
        return render_template('index.html', response=session['response'])
    else:
        print "case 3"
        return render_template('index.html', response=session['response'], winner=session['winner'])


@app.route('/guess', methods=['POST'])
def guess():
    guess = request.form['guess']
    winning_number = session['winning_number']
    if 'winner' in session:
        session.pop('winner')

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
        session['winner'] = "A new number has been selected. Start guessing to play again!"
        session.pop('winning_number')
        return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.pop('winning_number')
    return redirect('/')


app.run(debug=True)
