from flask import Flask, render_template, url_for, request, redirect,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def Base():
	if request.method == "POST":
		name = request.form["name"]
		email = request.form["email"]
		message = request.form["message"]
		return redirect(url_for('Thankyou'))
	else:
		return render_template('index.html') 
	

@app.route('/Thankyou', methods=["POST", "GET"])
def Thankyou():
    return render_template('Thankyou2.html')

if __name__ == "__main__":
	app.run(debug=True)