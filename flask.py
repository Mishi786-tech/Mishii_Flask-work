# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 18:22:38 2025

@author: L1F22PACS0008
"""

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"
@app.route('/contact')
def contact():
    return " This is the contact page."
@app.route('/about')
def about():
    return "This is the about page."

@app.route('/user/<name>')
def user(name):
    return f"hello, {name} !"



@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
@app.route('/form', methods=['GET','POST'])
def form():
    if request.method== 'POST':
        firstname= request.form['firstname']
        secondname= request.form['secondname']
        email= request.form['email']
        address= request.form['address']
        return render_template('Result.html' , firstname=firstname ,secondname=secondname,email=email ,address=address)
       # return f"hellow, {firstname , secondname, email, address}!"
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)
