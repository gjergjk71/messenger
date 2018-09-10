from flask import Flask,request,jsonify,render_template
from flaskext.mysql import MySQL
import bcrypt
import secrets
import os

app = Flask(__name__)
mysql = MySQL()
app.config["MYSQL_DATABASE_USER"] = os.environ.get("MYSQL_DATABASE_USER")
app.config["MYSQL_DATABASE_PASSWORD"] = os.environ.get("MYSQL_DATABASE_PASSWORD")
app.config["MYSQL_DATABASE_DB"] = os.environ.get("MYSQL_DATABASE_DB")
app.config["MYSQL_DATABASE_HOST"] = os.environ.get("MYSQL_DATABASE_HOST")
mysql.init_app(app)

def createToken(db,user_id):
	conn = db.connect()
	c = conn.cursor()
	token = secrets.token_urlsafe()
	c.execute("""INSERT INTO Token(token,user_id,status)
				 VALUES ('%s','%s','valid')""" % (token,user_id))
	conn.commit()
	conn.close()
	return token

def validate_get_Token(mysql,token):
	#return {"DSADAS1231232":"DSAD"}
	conn = mysql.connect()
	c = conn.cursor()
	c.execute("""SELECT token,user_id,status FROM Token
				 WHERE token='%s' LIMIT 1""" % token)
	token = c.fetchone()
	conn.close()
	if token:
		if token[2] == "valid":
			return token
	return False

def getUser(mysql,ID="",username=""):
	conn = mysql.connect()
	c = conn.cursor()
	if username:
		c.execute("""SELECT id,username FROM User
					 WHERE username='%s'""" % username)
	else:
		c.execute("""SELECT id,username FROM User
					 WHERE id='%s'""" % ID)	
	user = c.fetchone()
	conn.close()
	return user

def getMessages(mysql,conv_id):
	conn = mysql.connect()
	c = conn.cursor()
	c.execute("SELECT user_id,message,timestamp	FROM Message where conversation_id=%d" % (conv_id))
	messages = [list(message) for message in list(c.fetchall())]
	for message in messages:
		sender = getUser(mysql,message[0])
		message[0] = sender[1]
		
	conn.close()
	return messages

def createMessage(conversation_id,user_id,content):
	conn = mysql.connect()
	c = conn.cursor()
	c.execute("""INSERT INTO Message(message,conversation_id,user_id)
				 VALUES (%s,%d,%d)""" % content,conversation_id,user_id)
	conn.commit()
	conn.close()

@app.route("/api/login",methods=["GET","POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	username = request.form["username"]
	password = request.form["password"]
	conn = mysql.connect()
	c = conn.cursor()
	c.execute("SELECT id,username,password FROM User WHERE username='%s'" % username)
	print("DSA)")
	user = c.fetchone()
	conn.close()
	print(user)
	if user:
		if bcrypt.checkpw(password.encode("utf8"),eval(user[2])):
			token = createToken(mysql,user[0])
			json = {"bad_credentials":False,
					"logged_in":user[0],
					"username":user[1],
					"token":token}
			return jsonify(json) 
	json = {"bad_credentials":True}
	return jsonify(json)
	
@app.route("/api/register",methods=["GET","POST"])
def register():
	if request.method == "GET":
		return render_template("login.html")
	username = request.form["username"]
	password = request.form["password"]
	password_hashed = bcrypt.hashpw(password.encode("utf8"),bcrypt.gensalt())
	conn = mysql.connect()
	c = conn.cursor()
	c.execute("""INSERT INTO User(username,password)
				 VALUES ("%s","%s")""" % (username,password_hashed))
	conn.commit()
	conn.close()
	json = {"registered":True,"username":username}
	return jsonify(json) 

@app.route("/api/<string:token>/chat/<string:username>",methods=["GET","POST"])
def chat(token,username):
	token = validate_get_Token(mysql,token)
	conversation_id = "Not found"
	if not token:
		json = {"invalid_token":True}
		return jsonify(json)
	sender_id = token[1]
	receiver = getUser(mysql,username=username)
	if not receiver:
		json = {"receiver_not_found":True}
		return jsonify(json)
	receiver_id = receiver[0]
	conn = mysql.connect()
	c = conn.cursor()
	c.execute("SELECT conversation_id FROM Participant WHERE user_id=%d" % (sender_id,))
	senderConversations_id = c.fetchall()
	c.execute("SELECT conversation_id FROM Participant WHERE user_id=%d" % (sender_id,))
	receiverConversations_id = c.fetchall()
	for senderConversation_id in senderConversations_id:
		if senderConversation_id in receiverConversations_id:
			conversation_id = senderConversation_id[0]
			break
	conn.close()
	if conversation_id == "Not found":
		json = {"conversation_id":conversation_id}
		return jsonify(json)
	messages = getMessages(mysql,conversation_id)
	json = {"conversation_id":conversation_id,
			"messages":messages}
	return jsonify(json) 

@app.route("/api/validate_token/<string:token>",methods=["GET","POST"])
def validate_token(token):
	token_ = validate_get_Token(mysql,token)
	if token_:
		json = {"valid_token":True}
	else:
		json = {"valid_token":False}
	return jsonify(json)

@app.route("/api/<string:token>/create_message/<int:conversation_id>",methods=["POST"])
def create_message(token,conversation_id):
	token = validate_get_Token(mysql,token)
	if not token:
		json = {"invalid_token":True}
		return jsonify(json)
	content = request.form["content"]
	try:
		createMessage(conversation_id,token[2],content)
		json = {"successful":True}
	except:
		json = {"successful":False}
	return jsonify(json)


if __name__ == "__main__":
	app.run(port=8080,debug=True)
