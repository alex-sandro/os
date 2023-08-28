from flask import Flask, render_template

Flask = app(__name__)

@app.route("/")
def home():
    return render_template('index.html')