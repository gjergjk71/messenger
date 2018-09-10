import tkinter as tk
from ui.LoginWindow import LoginWindow
from ui.ChatWindow import ChatWindow
import requests

class MainWindow(LoginWindow):
	def __init__(self,master):
		super().__init__(master)
		self.chat_ui = ChatWindow(master)
		self.setupMainUI(master)
		self.master = master
		self.master.title("Messenger")
		self.w = 900 # width for the Tk root
		self.h = 600 # height for the Tk root

		# get screen width and height
		self.ws = master.winfo_screenwidth() # width of the screen
		self.hs = master.winfo_screenheight() # height of the screen

		# calculate x and y coordinates for the Tk root window
		self.x = (self.ws/2) - (self.w/2)
		self.y = (self.hs/2) - (self.h/2)

		# set the dimensions of the screen 
		# and where it is placed
		self.master.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
		self.showLogin()
	def setupMainUI(self,master):
		l1 = tk.Label(master,text="Messenger",font=("",50))
		l2  = tk.Label(master,text="Username: ",font=("",40))
		e1_text = tk.StringVar()
		e1 = tk.Entry(master,textvariable=e1_text,font=("",20))
		b1 = tk.Button(master,text="CHAT",font=("",20),command=lambda:self.chat(e1_text.get(),))
		self.mainWidgets = {"l1":l1,
							"l2":l2,
							"e1":e1,
							"b1":b1}
		self.mainTextVariables = {"e1_text":e1_text}
	def showMain(self):
		self.mainWidgets["l1"].place(x=50,y=50) 
		self.mainWidgets["l2"].place(x=100,y=150) 
		self.mainWidgets["e1"].place(x=400,y=170) 
		self.mainWidgets["b1"].place(x=350,y=230) 

	def hideMain(self):
		for widget_name,widget_instance in self.mainWidgets.items():
			widget_instance.place_forget()
	def login(self):
		login_api = "http://localhost:8080/api/login"
		credentials = {"username":self.loginTextVariables["e1_text"].get(),
					   "password":self.loginTextVariables["e2_text"].get()}
		response = requests.post(login_api,data=credentials)
		json = response.json()
		print(json)
		if json["bad_credentials"]:
			self.loginWidgets["label4"].place(x=150,y=130)
		else:
			with open("token","w") as file:
				file.write(json["token"])
			self.hideLogin()
			self.showMain()
		print("DSADSSADA321321321")
	def chat(self,receiver):
		with open("token") as file:
			token = file.readlines()[0]
			print(token)
			conversation_api = "http://localhost:8080/api/{}/chat/{}".format(token,receiver)
		print(conversation_api)
		response = requests.get(conversation_api)
		json = response.json()

		if json.get("receiver_not_found"):
			print("receiver_not_found")
		else:
			print(json)
			self.hideMain()
			self.chat_ui.showChat(receiver)