from flask import Flask, render_template, session, redirect, url_for, request
import mysql.connector  # installera med "pip install mysql-connector-python" i kommandotolken, ifall du inte redan gjort detta

app = Flask(__name__)
app.secret_key = 'hemligtextsträngsomingenkangissa'  # Används för sessionshantering

# skapa databasuppkoppling
def get_connection(host="localhost", user="root", password=""):
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database="webbserverprogrammering"  # byt namn om din databas heter något annat
    )
    return mydb
