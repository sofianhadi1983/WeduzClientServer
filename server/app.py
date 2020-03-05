from flask import Flask
from commons import main

app = Flask(__name__)

@app.route('/')
def say_hay():
    return 'Hello, world from AlphaServer'

@main
def run():
	app.run()