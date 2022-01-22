from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/404')
def error404():
    return render_template('404.html')

@app.route('/403')
def error403():
    return render_template('403.html')

@app.route('/500')
def error500():
    return render_template('500.html')

@app.route('/408')
def error408():
    return render_template('408.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def page_not_allowed(e):
    return render_template('403.html'), 403

@app.errorhandler(500)
def page_not_allowed(e):
    return render_template('500.html'), 500

@app.errorhandler(408)
def page_not_allowed(e):
    return render_template('408.html'), 408
