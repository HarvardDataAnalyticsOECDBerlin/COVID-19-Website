from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from datetime import datetime
from forms import LoginForm

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'thisShouldBeChanged!!'

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/donate')
def donate():
    return render_template('donation.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form = form)

# Making debugging and development easier (hot reload). Must remove when going to prod
if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)