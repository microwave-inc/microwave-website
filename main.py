#----- I M P O R T S -----#
from flask import Flask
from flask import render_template
from flask import abort, request
import random
#----- D E F I N E D   I T E M S -----#
randomport = random.randint(2000, 5899)
app = Flask(__name__)

#----- M A I N   P A G E S -----#
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/about')
def about():
  return render_template('portfolio.html')
#-----T E S T I N G   F O R   E R R O R S-----#
@app.route('/404')
def error404():
    return render_template('/errors/404.html')

@app.route('/403')
def error403():
    return render_template('/errors/403.html')

@app.route('/500')
def error500():
    return render_template('/errors/500.html')

@app.route('/408')
def error408():
    return render_template('/errors/408.html')
#----- S T A T I C   F I L E S -----#
@app.route('/logo.png')
def logo():
  return app.send_static_file('img/bot.png')
  
@app.route('/rock.png')
def rock_photo():
  return app.send_static_file('img/rock.png')
#----- E R R O R   H A N D L E R S -----#
@app.errorhandler(404)
def page_not_found(e):
    return render_template('/errors/404.html'), 404

@app.errorhandler(403)
def page_not_authorized(e):
    return render_template('/errors/403.html'), 403

@app.errorhandler(500)
def server_error(e):
    return render_template('/errors/500.html'), 500

@app.errorhandler(408)
def server_timeout(e):
    return render_template('/errors/408.html'), 408

@app.errorhandler(418)
def teapot(e):
    return render_template('/errors/joke.html'), 418
#----- E A S T E R   E G G S -----#
@app.route('/hidden')
def hidden():
    return render_template('/errors/joke.html')

@app.route('/what-is-this')
def egg():
    return teapot(418)
#----- F L A S K   S T A R T E R -----#
#This is for testing only
app.run(host='localhost', port=8080, debug=True)

#This is for deployment only
#app.run(host='0.0.0.0', port=80, debug=True)

#added fancy comments to show what each thing does
