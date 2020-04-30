from flask import Flask, render_template, url_for, redirect, request
from datetime import datetime
from forms import LoginForm
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/donate')
def donate():
    return render_template('donation.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form = form)

# Making debugging and development easier (hot reload). Must remove when going to prod
if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)