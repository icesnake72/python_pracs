
import random
import mysql.connector
from flask import Flask, render_template, redirect as rd, url_for


app = Flask(__name__)

mydb = mysql.connector.connect(
  host='localhost'
)


@app.route('/')
def index():
  print(Flask.default_config)
  return 'hi'

@app.route('/greetings/<id>')
def greet(id):
  return 'Hello : ' + id

@app.route('/crud/<user>')
def crud(user):
  with open('./templates/test.html', 'r') as html:
    doc = html.read()
  return doc

@app.route('/render')
def render_crud_template():
  return render_template('test.html')

@app.route('/<name>')
def welcom(name):
  return render_template('test.html', content=name)

@app.route('/redirect')
def redirect():
  newNum = random.randint(1,100)
  return rd(url_for('welcom', name=f'{newNum}'))
  

# if __name__ == '__main__':  
app.run(port=5001, debug=True)

