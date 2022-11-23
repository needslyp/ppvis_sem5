import psycopg2
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (jsonify, request)
import pandas as pd

app = Flask(__name__)

@app.route('/')
def authorization_page():
    return render_template('authorization.html')

@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

@app.route('/new_patient')
def new_patient():
    return render_template('new_patient.html')

@app.route('/form')
def form():
    return render_template('form.html', diagnos='Перелом', name='Иванов А.А.')

if __name__== "__main__":
    app.run(debug=True)