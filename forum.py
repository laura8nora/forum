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

    
