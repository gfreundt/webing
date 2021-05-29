import os
from flask import Flask, redirect, url_for, render_template, request
import json


def find_path():
    paths = [r'C:\Users\Gabriel Freundt\Google Drive\Multi-Sync\sharedData',r"D:\Google Drive Backup\Multi-Sync\sharedData", r"C:\users\gfreu\Google Drive\Multi-Sync\sharedData", '/home/pi/webing']
    for path in paths:
        if os.path.exists(path):
            return path

DATA_PATH = os.path.join(find_path(), 'data')

app = Flask(__name__)

@app.route("/tdc")
def tdc():
	return "<a href='http://190.117.62.94:65001/venta' <b>Esta página ha cambiado de dirección</b></p></a>"

@app.route("/venta")
def venta():
	with open(os.path.join(DATA_PATH, 'WEB_Venta.json'), mode='r') as file:
		data = json.load(file)
		details = data['details']
		details1, details2 = details[:len(details)//2], details[len(details)//2:]
		return render_template('venta.html', head=data['head'], details1=details1, details2=details2)

@app.route("/compra")
def compra():
	with open(os.path.join(DATA_PATH, 'WEB_Compra.json'), mode='r') as file:
		data = json.load(file)
		details = data['details']
		details1, details2 = details[:len(details)//2], details[len(details)//2:]
		return render_template('compra.html', head=data['head'], details1=details1, details2=details2)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    #app.run(debug=True)

