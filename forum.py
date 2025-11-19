from flask import Flask, render_template, session, redirect, url_for, request
import mysql.connector

app = Flask(__name__)
app.secret_key = 'mysecretkey'

def get_connection(host="localhost", user="root", password=""):
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database="webbserverprogrammering"
    )
    return mydb

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        logged_in = False
        db = get_connection()
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM users")
        users = mycursor.fetchall()
        for user in users:            
            if request.form['name'] == user[0] and request.form['password'] == user[1]:
                logged_in = True
                session['user'] = {'username': user[0], 'email': user[2]}
                break
        if not logged_in: 
            session.clear()
        return redirect(url_for('login'))    
    return render_template('home.html')

@app.route('/login')
def login():
    def login():
    if session:
        return render_template('login.html', user=session['user'])
    else:
        return render_template('error.html')

@app.route('/otherwebsie')
def otherwebsie():
    if session:
        db = get_connection()
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM posts ORDER BY time DESC")
        posts = mycursor.fetchall()
        return render_template('otherwebsie.html', user=session['user'], posts=posts)
    else:
        return render_template('error.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/append', methods=['POST'])
def append():
    if not session:
        return render_template('error.html')
    author = session['user']['username']
    text = request.form.get('line', '')
    now = datetime.datetime.now()
    db = get_connection()
    mycursor = db.cursor()
    sql = "INSERT INTO posts (author, text, time) VALUES (%s, %s, %s)"
    val = (author, text, now)
    mycursor.execute(sql, val)
    db.commit()
    return redirect('/otherwebsie')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
