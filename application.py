from flask import Flask, render_template, url_for, redirect, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/donate')
def donate():
    return render_template('donation.html')
