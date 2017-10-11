from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "s;ldjf;askjdf;kjsdlfjkskjfksjflejfijewef"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comments = request.form['comments']

        if len(name) < 1:
            flash("You didn't fill in your name!")
            return redirect('/')

        if len(comments) < 1:
            flash("You didn't fill out a comment!")
            return redirect('/')
        elif len(comments) > 120:
            flash("Your comment must be less than 120 characters!")
            return redirect('/')

        else:
            return render_template('/result.html', name=name, location=location, language=language, comments=comments)


app.run(debug=True)
