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
    return render_template('lyric404.html')

@app.route('/403')
def error403():
    return render_template('403.html')

@app.route('/500')
def error500():
    return render_template('500.html')

@app.route('/408')
def error408():
    return render_template('408.html')

@app.route('/lyric')
def lyric():
  return render_template('lyric404.html')

@app.route('/renders')
def renders():
  return render_template('renders.html')

@app.route('/renders/supra')
def supie():
  return render_template('supie.html')

@app.route('/renders/supra/purpmist')
def supierender():
  return render_template('supiepurpmist.html')

@app.route('/renders/supra/blackfog')
def supierender2():
  return render_template('supiemistblack.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('lyric404.html'), 404

@app.errorhandler(403)
def page_not_authorized(e):
    return render_template('403.html'), 403

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(408)
def server_timeout(e):
    return render_template('408.html'), 408

app.run(host='0.0.0.0', port=8080, debug=True)