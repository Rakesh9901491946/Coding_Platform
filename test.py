from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
@app.route('/coding')
def coding():
   
    return render_template('coding.html')
