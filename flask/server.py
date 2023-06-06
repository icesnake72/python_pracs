
import random
import mysql.connector
from flask import Flask, render_template, redirect as rd, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="$yewon0122$",
#   database="students"
# )

# mycursor = mydb.cursor()
# mycursor.execute('show tables')
# for x in mycursor:
#   print(x)
  
# sql = """create table 
# information (
#   id int not null auto_increment unique,
#   student_id int not null,
#   grade varchar(10) not null,
#   class varchar(10) not null,
#   height int,
#   weight int,
#   primary key(id)
# )
# """
# mycursor.execute(sql)
# mycursor.execute('show tables')
# for x in mycursor:
#   print(x)
  
# # information table의 student_id필드를 foreign_key로 만들기
# sql = """
# alter table information
# add constraint information_fid foreign key (student_id) references student(id)
# """
# mycursor.execute(sql)

# mycursor.execute('describe information')
# for x in mycursor:
#   print(x)


@app.route('/')
def index():
  print(Flask.default_config)
  return 'hi'

@app.route('/students')
def students():
  cur = mysql.connection.cursor()
  cur.execute('select * from student')
  data = cur.fetchall()
  cur.close()
  # print(data)
  
  lines = ''
  for rec in data:
    lines += '<p>'
    for col in rec:
      # print(col)
      lines += str(col)
      lines += '&nbsp;&nbsp;&nbsp;&nbsp;'
    lines + '</p>'
  return lines

# @app.route('/crud/<user>')
# def crud(user):
#   with open('./templates/test.html', 'r') as html:
#     doc = html.read()
#   return doc

# @app.route('/render')
# def render_crud_template():
#   return render_template('test.html')

# @app.route('/<name>')
# def welcom(name):
#   return render_template('test.html', content=name)

# @app.route('/redirect')
# def redirect():
#   newNum = random.randint(1,100)
#   return rd(url_for('welcom', name=f'{newNum}'))
  

if __name__ == '__main__':  
  app.secret_key = 'student_application_secret_key_25798237985792379582092042093437'
  app.config['MYSQL_HOST'] = 'localhost'
  app.config['MYSQL_USER'] = 'root'
  app.config['MYSQL_PASSWORD'] = '$yewon0122$'
  app.config['MYSQL_DB'] = 'students'
  mysql = MySQL(app)
  app.run(port=5001, debug=True)

