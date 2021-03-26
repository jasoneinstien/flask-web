#from app import app

from flask import Flask,redirect , url_for , render_template , request, session , flash ,g
#from markupsafe import escape

app = Flask(__name__)
app.secret_key = "admin"
app.config['TESTING'] = True
#app.testing = True
#app.config.from_object('yourapplication.default_settings')
#app.config.from_envvar('YOURAPPLICATION_SETTINGS')

#app.route(/login/<str:name>, methods = ["POST"])

admins = ['Tom']


#database setting 
def get_db():
	if 'db' not in g:
		g.db = sqlite3.connect(
			current_app.config['DATABASE'],
			detect_type = sqlite3.PARSE_DECLTYPES
		)
		g.db.row_factory = sqlite3.Row
	return g.db


@app.route('/' , methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form.get("nm")
        age = request.form.get("age")
        if name in admins:
        	if age == "10":
        		return f"hello {name} welcome back"
        	else:
        		return f"hello {name} you are {age} years old"
        else:
        	return redirect(url_for('username' , user=name))
    else:
    	return render_template('register.html')
        

@app.route('/login/<user>')
def username(user):
    return f"welcome {user}"

@app.route('/register' , methods = ['POST' , 'GET'])
def regs():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		if password == 'jason' and email == 'hello':
			return f"success"
		else:
			return f"fail"
	return render_template('reg.html') 

 

#@app.route('/register', methods = ['POST' , 'GET'])
#def regs():
#	con = app.config
#	#(app.config[secret_key])
#	return f'{con}'
	

@app.route('/usertesting/<username>')
def show_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('show_user.html', user=user)




if __name__ == "__main__":
    app.run(debug = True)
