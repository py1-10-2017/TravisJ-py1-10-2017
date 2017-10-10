from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'TeenageMutantNinjaTurtles2'


@app.route('/')
def index():
    session['message'] = "No Ninja's Here..."
    return render_template('index.html', message=session['message'])


@app.route('/ninja')
def ninja():
    #turtles2 = ['leonardo', 'donatello', 'michelangelo', 'raphael']
    turtles = [
        {'name': 'leonardo',
            'img': "/static/images/leonardo.jpg"},
        {'name': 'donatello',
            'img': "/static/images/donatello.jpg"},
        {'name': 'michelangelo',
            'img': "/static/images/michelangelo.jpg"},
        {'name': 'raphael',
            'img': "/static/images/raphael.jpg"}
    ]
    return render_template('turtles.html', turtles=turtles)


@app.route('/ninja/<color>')
def color(color):
    if color == 'blue':
        turtles = [{'name': 'leonardo',
                    'img': "/static/images/leonardo.jpg"}]
    elif color == 'orange':
        turtles = [{'name': 'michelangelo',
                    'img': "/static/images/michelangelo.jpg"}]
    elif color == 'red':
        turtles = [{'name': 'raphael',
                    'img': "/static/images/raphael.jpg"}]
    elif color == 'purple':
        turtles = [{'name': 'donatello',
                    'img': "/static/images/donatello.jpg"}]
    else:
        turtles = [{'name': 'Bad Casting of April',
                    'img': '/static/images/notapril.jpg'}]
    return render_template('turtles.html', turtles=turtles)


app.run(debug=True)
