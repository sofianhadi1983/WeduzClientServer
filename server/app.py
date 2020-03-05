from flask import Flask, render_template, request
from commons import main
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/')
def say_hay():
    data = db.all()
    return render_template('index.html', data=data)

"""
Request format:
{
    "server_name": "NodeABC",
    "total_login_attempts": 3
}
"""
@app.route('/log', methods=['POST'])
def recv_log_report():
    data = request.json
    server_name = data['server_name']
    total_login_attempts = data['total_login_attempts']
    
    Log = Query()
    res = db.search(Log.server_name == server_name)
    
    if len(res) > 0:
        #update data
        db.update({'total_login_attempts': total_login_attempts}, Log.server_name == server_name)
    else:
        #insert new data
        db.insert(data)
    
    return 'ok'

@main
def run():
	app.run()