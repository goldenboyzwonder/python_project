from flask import Flask, render_template # type: ignore
app = Flask(__name__)
title = 'Event Planner 1.0'
navTab = ['Dashboard','Customers','Appointments','Quotes']
@app.route('/')
def index():
    section = 'Dashboard'
    return render_template("index.html",title=title,section=section,navTab=navTab)
@app.route('/Customers')
def customers():
    tableHead = ['Customer','Contact','Event Type','Budget','Status','Created','Actions']
    return render_template("Customers.html",title=title,navTab=navTab,tableHead=tableHead)