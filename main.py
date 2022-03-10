from flask import Flask
from flask import render_template
from flask import Response
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

@app.route('/lyric')
def lyric():
  return render_template('/errors/lyric404.html')

@app.route('/about')
def about():
  return render_template('portfolio.html')

@app.route('/robots.txt')
def robots():
  return app.send_static_file('robots.txt')

@app.route('/logo.png')
def logo():
  return app.send_static_file('bot.png')

@app.route('/school/basic')
def basic():
  return render_template('/school/basic.html')

@app.route('/school/page2')
def page2():
  return render_template('/school/page2.html')

@app.route('/school/rock_climbing')
def rock_climbing():
  return render_template('/school/rock.html')

@app.route('/rock.png')
def rock_photo():
  return app.send_static_file('rock.png')

@app.route('/school/assesment')
def assesment():
  return render_template('/school/assesment.html')

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

app.run(host='0.0.0.0', port=randomport, debug=True)