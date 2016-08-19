from flask import Flask, render_template, request
import flask_sqlalchemy




app = Flask(__name__)

db = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/')
def inputPage():
    return render_template('input.html')

@app.route('/pagecomplete/', methods=['post'])
def completePage():

    tableNumber = request.form['tableNum']
    maker = request.form['maker']
    color = request.form['color']
    purpose = request.form['purpose']
    pagenum = request.form['pagenum']

    print(tableNumber, maker, color, purpose, pagenum)

    return render_template('complete.html')



app.run()