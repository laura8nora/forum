from flask import Flask, render_template, session, redirect, url_for, request
import mysql.connector

app = Flask(__name__)
app.secret_key = 'hemligtextsträngsomingenkangissa'

def get_connection(host="localhost", user="root", password=""):
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database="webbserverprogrammering"
    )
    return mydb
