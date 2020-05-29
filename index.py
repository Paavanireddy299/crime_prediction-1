def func(Latitude,Longitude,Date,Time):
	class1=["Robbery","Gambling","Accident","Violence","Kidnapping","Murder"]
	Year=float(Date[0:4])
	Month=float(Date[5:7])
	Day=float(Date[8:10])
	Hours=float(Time[0:2])
	Minutes=float(Time[3:5])
	print(Year,Month,Day,Hours,Minutes)
	loaded_model = pickle.load(open('model.sav', 'rb'))
	result = loaded_model.predict([[Latitude, Longitude,Year,  	Month,	Day, Hours,	Minutes]])
	p=result[0]
	p=list(p)
	p1=p.index(max(p))
	da=class1[p1]
	p2="After Processing the above details We can predict that at the specified coordinates and the give time their is a probability of "
	data=p2+da
	return render_template("form.html",data=data)



from flask import *
app=Flask(__name__)

import os
import pickle

@app.route('/')
def main_tem():
    return render_template("home.html")

@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/form_insert',methods=['GET','POST'])
def form_insert():
    Latitude= request.form['Latitude']
    Longitude = request.form['Longitude']
    Date = request.form['Date']
    Time = request.form['Time']
    print(Latitude)
    print(Longitude)
    print(Date)
    print(Time)
    p=func(Latitude,Longitude,Date,Time)
    return p



if __name__ =="__main__":
    app.run(debug=True)