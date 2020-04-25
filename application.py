from flask import Flask, render_template, url_for, redirect, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/healthCare')
def healthCare():
    return render_template('healthCare.html')
