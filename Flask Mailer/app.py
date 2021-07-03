from flask import Flask,render_template, request
import smtplib

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/result", methods = ["GET", "POST"])
def result():
	if(request.method == "POST"):
		sender = request.form.get("sender")
		password = request.form.get("password")
		reciever = request.form.get("reciever")
		message = request.form.get("message")
		server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
		server.ehlo()
		server.login(sender, password)
		server.sendmail(sender, reciever, message)
		server.close()
		return render_template("result.html")
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug = True)