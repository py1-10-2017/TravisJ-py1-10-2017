from flask import Flask, render_template, redirect, session, request


app = Flask(__name__)
app.secret_key = 'MySecretKey'


@app.route('/')
def main():
    import random
    # Set a random number
    winningNum = random.randrange(0, 11)
    session['winningNum'] = winningNum
    #response = session['response']
    print "The answer is:", winningNum
    session['count'] = 0

    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['count'] += 1
    guess = request.form['guess']
    winningNum = session['winningNum']

    if guess > winningNum:
        print "Too high"
        session['response'] = 'Too high!'
        return redirect('/')

    if guess < winningNum:
        print "Too low"
        session['response'] = 'Too low!'
        return redirect('/')

    if guess == winningNum:
        print "You win"
        session['response'] = "You win! Nice job!"
        return redirect('/')


app.run(debug=True)
