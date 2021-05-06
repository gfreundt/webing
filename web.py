import os
from flask import Flask, redirect, url_for, render_template, request
import updater
import datetime as dt
import time
import csv


def find_path():
    paths = [(r'C:\Users\Gabriel Freundt\Webing',r"D:\Webing", r"C:\users\gfreu\Webing"), (r'C:\Users\Gabriel Freundt\Google Drive\Multi-Sync\sharedData',r"D:\Google Drive Backup\Multi-Sync\sharedData", r"C:\users\gfreu\Google Drive\Multi-Sync\sharedData")]
    for k, path in enumerate(paths[1]):
        if os.path.exists(path):
            return paths[0][k], paths[1][k]

app_path, data_path = find_path()
DATA_PATH = os.path.join(data_path, 'data')
HTML_PATH = os.path.join(app_path)
CSS_PATH = os.path.join(app_path)

print(HTML_PATH)


app = Flask(__name__) #, template_folder=HTML_PATH) #, static_folder=CSS_PATH)

@app.route("/dog")
def index():
	with open(os.path.join(DATA_PATH, 'TDC_fixed.txt'), mode='r') as file:
		data = [i for i in csv.reader(file, delimiter=',')]
		promedio, promedio_time, promedio_date = data[0]
		latest = data[1:]
		return render_template('index.html', latest=latest, promedio=promedio, promedio_date=promedio_date, promedio_time=promedio_time)

#return render_template("dashboard.html", date=date, time=time, data=data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

