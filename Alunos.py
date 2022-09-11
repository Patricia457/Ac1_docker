import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'paty123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html.html')

@app.route('/gravarAluno', methods=['POST','GET'])
def gravarAluno():
  nome = request.form['nome']
  email = request.form['email']
  ra = request.form['ra']
  if nome and email and ra:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_Alunos (nome, email, ra) VALUES (%s, %s, %s)', (nome, email, ra))
    conn.commit()
  return render_template('index.html.html')


@app.route('/lista', methods=['POST','GET'])
def lista():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select nome, email, ra from tbt_Alunos')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)