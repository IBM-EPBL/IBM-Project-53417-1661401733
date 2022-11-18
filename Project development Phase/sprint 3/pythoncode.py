# importing the necessary dependencies
from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
import os

model = pickle.load(open('flight.pkl'.'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction',methods =['POST'])

def predict():
name = request.form['name']
month = request.form['month']
dayofmonth = request.form['dayofmonth']
dayofweek = request.form['dayofweek']
origin = request.form['origin']
if (origin == "msp"):
     origin1, origin2, origin3, origin4, orgin5 = 0,0,0,0,1
if (origin == "dtw"):
     origin1, origin2, origin3, origins4, orgin5 = 1,0,0,0,0
if (origin == "jfk"):
     origin1, origin2, origin3, origins4, orgins5 = 0,0,1,0,0
if (origin == "gea"):
     origin1, origin2, origin3, origins4, orgins5 = 0,1,0,0,0
if (origin == "alt"):
     origin1, origin2, origin3, origine4, orgin5 = 0,0,0,1,0

destination =  request.form['destination']
if (destination == "map"):
     destination1, destination2, destination3, destination4, destination5 = 0,0,0,0,1
if (destination == "dtw"):
     destination1, destination2, destinations3, destination4, destination5 = 1,0,0,0,0
if (destination == "jfk"):
     destination1, destination2, destination3, destination4, destination5 = 0,0,1,0,0
if (destination == "sea"): I
     destination1, destination2, destination3, destination4,destination5 = 0,1,0,0,0
if (destination == "alt"):
    destination1, destination2, destination3, destination4, destination5 = 0,0,0,1,0
dept =  request.form['dept')
arrtime = request.form['arrtime']
actdept = request.form['actdept')
dept15=int (dept)-int (actdept)
total = [[name, month, dayofmonth, dayofweek, origin1, origin2, origin3,origin4,origin5, destination1, destination2, destination3, destination4, destinations5, i
#print (total)
y pred model.predict(total)

print (y pred)

if(y_pred==[0.];
       ans="The Flight will be on time"
else
       ans="The Flight will be delayed"
return render_template ("index.html", showcase == ana)
