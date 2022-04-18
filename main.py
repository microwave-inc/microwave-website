from flask import Flask
from flask import render_template

import random
randomport = random.randint(2000, 9000)

app = Flask(__name__)
  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/404')
def error404():
    return render_template('/errors/lyric404.html')

@app.route('/403')
def error403():
    return render_template('/errors/403.html')

@app.route('/500')
def error500():
    return render_template('/errors/500.html')

@app.route('/408')
def error408():
    return render_template('/errors/408.html')

@app.route('/about')
def about():
  return render_template('portfolio.html')

@app.route('/logo.png')
def logo():
  return app.send_static_file('img/bot.png')
  
@app.route('/rock.png')
def rock_photo():
  return app.send_static_file('img/rock.png')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('/errors/lyric404.html'), 404

@app.errorhandler(403)
def page_not_authorized(e):
    return render_template('/errors/403.html'), 403

@app.errorhandler(500)
def server_error(e):
    return render_template('/errors/500.html'), 500

@app.errorhandler(408)
def server_timeout(e):
    return render_template('/errors/408.html'), 408

#This is for testing only
app.run(host='localhost', port=8080, debug=True)

#This is for deployment only
#app.run(host='0.0.0.0', port=randomport, debug=True)
