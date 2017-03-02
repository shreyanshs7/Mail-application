from flask import Flask,render_template,request,flash,url_for,redirect
from flask_mail import Mail, Message




app = Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'shreyanshss7@gmail.com'
app.config['MAIL_PASSWORD'] = 'shreyanshthess7'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
	return render_template('form.html')


@app.route('/form', methods=['POST','GET'])
def form():
	if request.method=="POST":
		name=request.form["name"]
		city=request.form["city"]
		email=request.form["email"]
		address=request.form["address"]
		pin=request.form["pin"]
		
		msg = Message('%s' % (name), sender='shreyanshss7@gmail.com' , recipients=['%s' % (email)])
		msg.body = "Name :- %s , City :- %s , Address :- %s , Pin :- %s" % (name,city,address,pin) 
		mail.send(msg)
		return "An e-mail has been sent to your e-mail id"
	return render_template('form.html')	
if __name__ == '__main__':
	app.run(debug=True)
