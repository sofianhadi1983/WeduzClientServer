from flask import Flask, render_template
from commons import main
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/')
def say_hay():
    data = db.all()
    return render_template('index.html', data=data)

@main
def run():
	app.run()