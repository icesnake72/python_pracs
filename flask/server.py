
import random
import mysql.connector
from flask import Flask, render_template, redirect as rd, url_for, request, session
from flask_mysqldb import MySQL, MySQLdb


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

def get_todos(id_:str):
  print(type(id_))
  print(id_)
  cur = mysql.connection.cursor()
  sql = 'select todo_name, created_time, done from todos where user_id=%s'
  
  values= (id_, )
  cur.execute(sql, values)
  todos = cur.fetchall()
  cur.close()
  return todos

@app.route('/')
def index():
  if session.get('userID'):
    todos = get_todos(session.get('id_'))
    return render_template('index.html', username=session.get('nick'), signin=True, todos=todos)
  
  return render_template('index.html', signin=False)
  # return '<h1>hello flask</h1>'

@app.route('/signin')
def signin():
  return render_template('signin.html')

@app.route('/logout')
def logout():
  session.pop('userID')
  session.pop('nick')
  session.pop('id_')
  return rd('/')

@app.route('/process_signin', methods=['post'])
def proc_sign_in():
  email_id_ = request.form.get('email_id')
  password_ = request.form.get('password')
  cur = mysql.connection.cursor()
  sql = 'select * from users where email=%s and password=%s'
  values = (email_id_, password_)
  cur.execute(sql, values)
  data = cur.fetchall()
  cur.close()
  if len(data):
    for row in data:
      print(row)
      nick_ = row[3]
      id_ = row[0]
        
    session['userID'] = email_id_
    session['nick'] = nick_
    session['id_'] = id_
    return rd('/')
  
  return '로그인 실패 : <a href="/signin">로그인 페이지로 돌아가기</a>'


@app.route('/signup')
def sign_up():
  return render_template('signup.html')

@app.route('/process_signup', methods=['post'])
def proc_sign_up():
  email_id_ = request.form.get('email_id')
  password_ = request.form.get('password')
  nick_name_ = request.form.get('nick_name')
  print(email_id_, password_, nick_name_)
  sql = '''insert into users(email, password, nick_name)
  values(%s,%s,%s)'''
  values = (email_id_, password_, nick_name_)
  cur = mysql.connection.cursor()
  try:
    cur.execute(sql, values)
    mysql.connection.commit()
    cur.close()
  except MySQLdb.IntegrityError as err:
    return f'회원가입 실패(이미 가입된 회원이 있음) : <a href="/">홈으로</a>'
  except:
    return f'회원가입 실패 : <a href="/">홈으로</a>'
    
  return '회원가입 성공 : <a href="/signin">로그인 페이지로 돌아가 로그인을 해주세요.</a>'


@app.route('/process_insert_todo', methods=['post'])
def insert_todo():
  todo = request.form.get('todo')
  sql = '''insert into todos (todo_name, user_id) values(%s, %s)'''
  values = (todo, session.get('id_'))
  cur = mysql.connection.cursor()
  try:
    cur.execute(sql, values)
    mysql.connection.commit()
    cur.close()
  except:
    return '''입력 실패 : <a href='/'>홈으로가기</a>'''
  
  return rd('/')
  
  

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
  app.config['MYSQL_PASSWORD'] = 'yewon0122'
  app.config['MYSQL_DB'] = 'todos'
  mysql = MySQL(app)
  app.run(port=5001, debug=True)

