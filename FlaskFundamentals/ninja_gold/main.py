from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '32131351561651'

import random
import datetime


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['places'] = []

    return render_template('index.html', session=session['gold'], places=session['places'])


@app.route('/process_money', methods=['POST'])
def process_money():
    ts = datetime.datetime.now()

    if request.form['place'] == 'farm':
        gold = random.randrange(10, 20)
        print gold
        exp = {}
        exp['place'] = 'farm'
        exp['gold'] = gold
        exp['time'] = ts
        exp['win'] = True

        session['gold'] += gold
        session['places'].append(exp)
        return redirect('/')

    elif request.form['place'] == 'cave':
        gold = random.randrange(5, 10)
        print gold
        exp = {}
        exp['place'] = 'cave'
        exp['gold'] = gold
        exp['time'] = ts
        exp['win'] = True

        session['gold'] += gold
        session['places'].append(exp)
        return redirect('/')

    elif request.form['place'] == 'house':
        gold = random.randrange(2, 5)
        print gold
        exp = {}
        exp['place'] = 'house'
        exp['gold'] = gold
        exp['time'] = ts
        exp['win'] = True

        session['gold'] += gold
        session['places'].append(exp)
        return redirect('/')

    else:
        chance = random.randrange(1, 3)
        gold = random.randrange(0, 50)
        place = 'casino'
        print chance

        if chance == 1:
            exp = {}
            exp['place'] = place
            exp['gold'] = gold
            exp['time'] = ts
            exp['win'] = False

            session['gold'] -= gold
            session['places'].append(exp)
            return redirect('/')
        else:
            exp = {}
            exp['place'] = place
            exp['gold'] = gold
            exp['time'] = ts
            exp['win'] = True

            session['gold'] += gold
            session['places'].append(exp)
            return redirect('/')


# added a reset function
@app.route('/reset', methods=['POST'])
def reset():
    session.pop('gold', 'places')
    return redirect('/')


app.run(debug=True)
