from flask import Flask, render_template, url_for, redirect, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/donate')
def donate():
    return render_template('donation.html')

# Making debugging and development easier (hot reload). Must remove when going to prod
if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)