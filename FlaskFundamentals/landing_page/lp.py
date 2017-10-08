from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninja')
def ninjas():
    return render_template('ninja.html')


@app.route('/dojos/new')
def new():
    return render_template('dojos/new.html')


app.run(debug=True)
