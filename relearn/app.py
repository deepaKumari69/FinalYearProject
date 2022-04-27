from flask import Flask, flash, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re ,os
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
# from consonants import single_prediction
import tensorflow as tf
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from binascii import a2b_base64
from flask import Flask
from flask_mail import Mail, Message

classifier = tf.keras.models.load_model('./Model_CNN_DevanagariHandWrittenCharacterRecognition.h5')
classifier1 = tf.keras.models.load_model('./CNN_vowel_model.h5')
classifier2 = tf.keras.models.load_model('./CNN_model_bengali.h5')



def single_prediction(test_img):
	
	test_img_arr = image.img_to_array(test_img)
	test_img_arr = np.expand_dims(test_img_arr, axis = 0)
	
	prediction = classifier.predict(test_img_arr)
	
	result = np.argmax(prediction[0])
	
	acc = round(prediction[0][np.argmax(prediction[0])]*100,3)
	#print(acc)
	
	res = classifier.predict([test_img_arr])[0]
	#print(res, np.argmax(res), max(res))
	return np.argmax(res)
def vowel_single_prediction(test_img):
	
	test_img_arr = image.img_to_array(test_img)
	test_img_arr = np.expand_dims(test_img_arr, axis = 0)
	
	prediction = classifier1.predict(test_img_arr)
	
	result = np.argmax(prediction[0])
	
	acc = round(prediction[0][np.argmax(prediction[0])]*100,3)
	#print(acc)
	
	res = classifier1.predict([test_img_arr])[0]
	#print(res, np.argmax(res), max(res))
	return np.argmax(res)

def b_single_prediction(test_img):
	
	test_img_arr = image.img_to_array(test_img)
	test_img_arr = np.expand_dims(test_img_arr, axis = 0)
	
	prediction = classifier2.predict(test_img_arr)
	
	result = np.argmax(prediction[0])
	
	acc = round(prediction[0][np.argmax(prediction[0])]*100,3)
	
	res = classifier2.predict([test_img_arr])[0]
	# print(res, np.argmax(res), max(res))
	return np.argmax(res)

	

UPLOAD_FOLDER = join(dirname(realpath(__file__)), './static/assets/images/quizes/')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','mp3'}


app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your_email'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'relearn'


mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM users WHERE email = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['username'] = account['username']
			msg = 'Logged in successfully !'
			#flash("Logged in successfully !")
			if account['role'] == 1:
				return render_template('index.html', msg = msg)
			else : 
				cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
				cursor.execute('SELECT * FROM quiz')
				account = cursor.fetchall()
				return render_template('admin/index.html', msg = account)

		else:
			flash("Incorrect Username or Password !","error")
			#msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')
	
@app.route('/admin')
@app.route('/admin/index')
def admin_index():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM quiz')
		account = cursor.fetchall()
		return render_template('admin/index.html', msg = account)
	else : return redirect(url_for('login'))
			
@app.route('/admin/course')
def course():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM course')
		account = cursor.fetchall()
		return render_template('admin/course.html', msg = account)
	else : return redirect(url_for('login'))

@app.route('/admin/addcourse' , methods=['POST'])
def add_course():
	if 'loggedin' in session:
		if request.method == "POST":
			level = request.form['level']
			link = request.form['link']	
			name = request.form['name']
			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute('INSERT into course (`name`,`link` , `level`) VALUES (% s, % s , % s)' ,(name,link,level) )
			mysql.connection.commit()
			flash('Lesson Added')
			return redirect(url_for('course')) 
	else : return redirect(url_for('login'))
			
@app.route('/admin/progress')
def progress():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT p.id, u.username,p.course_id ,p.level  from progress p , users u where p.uid = u.id')
		account = cursor.fetchall()
		return render_template('admin/progress.html', msg = account)
	else : return redirect(url_for('login'))
			
@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	flash("Logged out successfully !", "success")
	return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		name = request.form['name']
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM users WHERE email = % s', (email, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not re.match(r'[A-Za-z0-9]+', name):
			msg = 'name must contain only characters and numbers !'
		else:
			cursor.execute('INSERT INTO users(`name`,`username`,`password`,`email`) VALUES ( % s, % s, % s, % s)', (name,username, password, email, ))
			mysql.connection.commit()
			id = cursor.lastrowid
			cursor.execute('INSERT INTO progress(`course_id`,`uid`) VALUES ( % s, % s)', (1,id ))
			cursor.execute('INSERT INTO progress(`course_id`,`uid`) VALUES ( % s, % s)', (2,id ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
			return redirect(url_for('login'))
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)

@app.route("/index")
def index():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM  users' )
		account = cursor.fetchone()	
		return render_template("index.html",msgs = account)
	else : return redirect(url_for('login'))

@app.route("/update", methods =['GET', 'POST'])
def update():
	msg = ''
	if 'loggedin' in session:
		if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
			username = request.form['username']
			password = request.form['password']
			email = request.form['email']
			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute('SELECT * FROM users WHERE username = % s', (username, ))
			account = cursor.fetchone()
			if account:
				msg = 'Account already exists !'
			elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
				msg = 'Invalid email address !'
			elif not re.match(r'[A-Za-z0-9]+', username):
				msg = 'name must contain only characters and numbers !'
			else:
				cursor.execute('UPDATE users SET username =% s, password =% s, email =% s, WHERE id =% s', (username, password, email,(session['id'], ), ))
				mysql.connection.commit()
				msg = 'You have successfully updated !'
		elif request.method == 'POST':
			msg = 'Please fill out the form !'
		return render_template("update.html", msg = msg)
	else : return redirect(url_for('login'))

@app.route('/choose' , methods=['POST'])
def language () :
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	if not "id" in request.form  :
		id = request.form['course_id']
		cursor.execute('update `progress` set level = level+1 where course_id = %s and uid = %s ',(id,session['id'] ) )
		mysql.connection.commit()
	else : id = request.form['id']
	print("ID : ",id)
	cursor.execute('SELECT level from progress where uid = %s and course_id =  %s ', (session['id'], id ))
	account = cursor.fetchone()
	return render_template('level.html' ,msg = account,lang = id, e=True)

@app.route('/users')
def manage_users () :
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT `id`,`name`,`username`,`email`,`password`,`role` FROM users')
		account = cursor.fetchall()
		if 'delete' in session:
			return render_template('admin/users.html',msg= account)
		else : return render_template('admin/users.html',msg= account)
	else : return redirect(url_for('login'))

# @app.route('/learn/<string:question>',methods=['GET'])
@app.route('/learn/<string:no>',methods=['POST'])
def learn (no) :
	print(request.values)
	no = no
	level = request.form['level']			
	course_id = request.form['course_id']			
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT *  FROM course where level = %s and name = %s' ,( level,course_id))
	print('SELECT * FROM course where level = %s and name = %s' ,( level,course_id))	
	account = cursor.fetchall()
	return render_template('learn.html',msg = account,id = course_id ,count =len(account) ,no=int(no),level=level ,e=True)

@app.route('/practice/<string:no>',methods=['POST'])
def practice (no) :
	no = no
	level = request.form['level']			
	course_id = request.form['course_id']			
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT *  FROM practice where level = %s and `course` = %s' ,( level,course_id))
	print('SELECT * FROM practice where level = %s and `course` = %s' ,( level,course_id))	
	account = cursor.fetchall()
	print(account)
	return render_template('practice.html',msg = account,id = course_id ,count =len(account) ,no=int(no),level=level ,e=True)
	
@app.route('/quiz/<string:no>',methods=['POST'])
def quiz (no) :
	no = no
	level = request.form['level']			
	course_id = request.form['course_id']			
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT *  FROM quiz where level = %s and `course_id` = %s' ,( level,course_id))
	print('SELECT * FROM quiz where level = %s and `course_id` = %s' ,( level,course_id))	
	account = cursor.fetchall()
	print(account)
	return render_template('quiz.html',msg = account,id = course_id ,count =len(account) ,no=int(no),level=level ,e=True)
	

@app.route('/admin/practice',methods = ['POST', 'GET'])
def admin_practice () :
	if 'loggedin' in session:	
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT `id`,`course`,`level`,`file`,`correct`,`model` FROM practice')
		account = cursor.fetchall()
		return render_template('admin/practice.html',msg = account)
	else : return redirect(url_for('login'))

@app.route('/admin/add-p',methods =['POST'])
def add_practice() :
		
	if 'loggedin' in session:
		if request.method == 'POST' :
			language = request.form['language']
			level = request.form['level']
			correct = request.form['correct']
			model = request.form['model']
			f = request.files['audio']

			f.save(os.path.join(join(dirname(realpath(__file__)), './static/assets/audios/', secure_filename(f.filename))))

			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute(' INSERT into practice (`course`,`file`,`correct`,`level`,`model`) values ( % s , % s ,% s , % s, % s) ',(language,f.filename,correct,level,model ))
			mysql.connection.commit()
			flash("Question inserted")
			# print(request.form)
			return redirect(url_for('admin_practice'))
		else : return redirect(url_for('admin_practice'))
	else : return redirect(url_for('login'))

@app.route('/admin/add',methods =['GET', 'POST'])
def add () :
		
	if 'loggedin' in session:
		if request.method == 'POST' :
			language = request.form['language']
			question = request.form['question']
			level = request.form['level']
			s = request.form.getlist('option')
			options = ' '.join([str(elem) for elem in s])
			correct = request.form['correct']
			print(request.form)
			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			f = request.files['image']
			if len(f.filename)> 0 :
				f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
				cursor.execute(' INSERT into quiz (`course_id`,`question`,`options`,`correct`,`level` , `image`) values ( % s , % s ,% s , % s, % s, % s) ',(language,question,options,correct,level, f.filename))
			else :	cursor.execute(' INSERT into quiz (`course_id`,`question`,`options`,`correct`,`level` ) values ( % s , % s ,% s , % s, % s) ',(language,question,options,correct,level))
			mysql.connection.commit()
			flash("Question inserted")
			# print(request.form)
			return render_template('admin/add.html')
		else : return render_template('admin/add.html')
	else : return render_template('quiz.html')
	
@app.route('/delete/<string:id>',methods =['GET'])
def delete_user(id):
	
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('DELETE FROM %s WHERE id = %s' % ("users", id))	
	mysql.connection.commit()
	flash("User Deleted Successfully!","success")
	return redirect(url_for('manage_users'))
		
@app.route('/admin/delete-course/<string:id>',methods =['GET'])
def delete_course(id):
	if 'loggedin' in session:	
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('DELETE FROM %s WHERE id = %s' % ("course", id))	
		mysql.connection.commit() 
		flash("Lesson Deleted Successfully!","success")
		return redirect(url_for('course'))
	else : return redirect(url_for('login'))

@app.route('/admin/delete-practice/<string:id>',methods =['GET'])
def delete_practice(id):
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('DELETE FROM %s WHERE id = %s' % ("practice", id))
		print('DELETE FROM %s WHERE id = %s' % ("practice", id))	
		mysql.connection.commit()
		flash("Deleted Successfully!","success")
		return redirect(url_for('admin_practice'))
	else : return redirect(url_for('login'))
		
@app.route('/image' , methods= ['POST'])
def save_image() : 
	if 'loggedin' in session:
		if request.method == "POST" :	
			level = request.form['level']
			course_id = request.form['course_id']
			no = request.form['no']
			f = request.form['image_url']
			binary_data = a2b_base64(f)
			a = str(session['id'])
			filename = join(f"input-{a}.png")
			fd = open(filename, 'wb')
			fd.write(binary_data)
			fd.close()
			index = int(no)
			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute('SELECT *  FROM practice where level = %s and `course` = %s' ,( level,course_id))
			print('SELECT * FROM practice where level = %s and `course` = %s' ,( level,course_id))	
			account = cursor.fetchall()
			count = len(account);
			test_img = image.load_img(filename, target_size = (32, 32, 3))
			if account[index]['model'] == 2 :
				res = b_single_prediction(test_img)		
			elif account[index]['model'] == 0 :
				res = single_prediction(test_img)		
			else :	res = vowel_single_prediction(test_img)	
			if account[index]['correct'] == res : 
				flash('Correct Letter Drawn ! ')
				return redirect(url_for('practice',no=int(no)),code=307)
			else: 
				flash('Wrong Letter Drawn ! ') 
				print(f"Res = {res}, Correct = ",account[index]['correct'])
				return redirect(url_for('practice',no=int(no)),code=307)
	else : return redirect(url_for('login'))

@app.route('/admin/qdelete/<string:id>',methods =['GET'])
def delete_question(id):
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('DELETE FROM %s WHERE id = %s' % ("quiz", id))	
		mysql.connection.commit()
		flash("Question Deleted ")
		return redirect(url_for('admin_index'))
	else : return redirect(url_for('login'))		

@app.route('/language' , methods=['GET','POST'])
def c_language() : 
	if 'loggedin' in session:
		return render_template('c_language.html')
	else : return redirect(url_for('login'))

@app.route('/load',methods=['POST'])
def load():
	if 'loggedin' in session:
		level = request.form['level']
		course = request.form['course']
		print("level is ", level)
		return render_template('language.html',level = level,id = course)
	else : return redirect(url_for('login'))

@app.route('/check',methods=['GET'])
def check():
	if 'loggedin' in session:
		level = request.form['level']
		course = request.form['course']
		print("level is ", level)
		return render_template('language.html',level = level,id = course)
	else : return redirect(url_for('login'))


@app.route('/imgtest',methods=['POST'])
def test_img():
	f = request.form['image_url']
	binary_data = a2b_base64(f)
	fname  = os.path.join(join(dirname(realpath(__file__)), './static/assets/images/practice/input-',str(session['id']),'.png'))
	f.save()
	fd = open(fname, 'wb')
	fd.write(binary_data)
	fd.close()
	return "Done"

@app.route('/move',methods = ['POST'] )
def move():
	no = request.form['no']
	level = request.form['level']
	course_id = request.form['course_id']
	index = int(no)
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT *  FROM practice where level = %s and `course` = %s' ,( level,course_id))
	account = cursor.fetchall()
	count = len(account);
	if (count-(index+1)) > 0 :
		return redirect(url_for('practice',no=int(no)+1),code=307)
	else: 
		return redirect(url_for('quiz',no=0),code=307)
@app.route('/fpass',methods = ['POST'] )
def forgotpass():
	new = request.form['new']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute("update `users` set password = '%s' where id = %s" % ( new,session['id']))
	mysql.connection.commit()
	flash('Password Updated ')
	return redirect(url_for('myprogress'))
@app.route('/forgotpass' )
def fpass():
	return render_template('fpass.html')
@app.route('/upass',methods = ['POST'] )
def updatepass():
	old = request.form['old']
	new = request.form['new']
	cnf = request.form['confirm']
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute('SELECT *  FROM users where id = %s',(session['id'],))
	row = cursor.fetchone()
	if(old != row['password']):
		flash('Original Password does not match!', "error")
	elif(new != cnf):
		flash('New Password and Confirm New Password does not match!', "error")
	else:
		cursor.execute("update `users` set password = '%s' where id = %s" % ( new,session['id']))
		mysql.connection.commit()
		flash('Password updated successfully!', "success")
	return redirect(url_for('myprogress'))
	
@app.route('/myprogress',methods = ['GET','POST'] )
def myprogress():
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	# print('SELECT *  FROM progress where `uid` = %s' ,( session['id']))
	cursor.execute('SELECT *  FROM users where `id` = %d' % ( session['id']))
	account = cursor.fetchall()
	cursor.execute('SELECT level  FROM progress where `uid` = %d Order by course_id' % ( session['id']))
	course = cursor.fetchall()
	return render_template('progress.html',msg = account,marathi = course[0] , bengali = course[1])
	
@app.route("/mail" ,methods=['POST'])
def mailer():
	email = request.form['email'] 
	cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
	cursor.execute(f"SELECT name, password FROM users WHERE email = '{email}'")
	account = cursor.fetchone()
	passw = account['password'];
	usernm = account['name'];
	msg = Message('Password Recovery - Relearn', sender = app.config['MAIL_USERNAME'], recipients = [email])
	msg.body = f"Hello {usernm},\nWe have received a password recovery request for your Relearn account.\nYour original password is {passw}"
	mail.send(msg)
	flash("Original Password is sent to your registered email!","success")
	return redirect(url_for('fpass'))
