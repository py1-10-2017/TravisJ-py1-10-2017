from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'TeenageMutantNinjaTurtles1'


@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
