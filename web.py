import os
from flask import Flask, redirect, url_for, render_template, request
import datetime as dt
import time
import csv


def find_path():
    paths = [r'C:\Users\Gabriel Freundt\Google Drive\Multi-Sync\sharedData',r"D:\Google Drive Backup\Multi-Sync\sharedData", r"C:\users\gfreu\Google Drive\Multi-Sync\sharedData", '/home/pi/webing']
    for path in paths:
        if os.path.exists(path):
            return path

DATA_PATH = os.path.join(find_path(), 'data')

app = Flask(__name__)

@app.route("/tdc")
def index():
	with open(os.path.join(DATA_PATH, 'TDC_fixed.txt'), mode='r') as file:
		data = [i for i in csv.reader(file, delimiter=',')]
		promedio, promedio_time, promedio_date = data[0]
		latest = data[1:]
		images, urls, quotes = [i[0] for i in latest], [i[1] for i in latest], [i[2] for i in latest]
		images1, images2 = images[:len(images)//2], images[len(images)//2:]
		quotes1, quotes2 = quotes[:len(quotes)//2], quotes[len(quotes)//2:]

		print(images1,images2)
		print(quotes1,quotes2)
		return render_template('index.html', quotes1=quotes1, quotes2=quotes2, images1=images1, images2=images2, urls=urls, promedio=promedio, promedio_date=promedio_date, promedio_time=promedio_time)

#return render_template("dashboard.html", date=date, time=time, data=data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

