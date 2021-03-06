from error_handlers import handle_requests_errors
import tkinter as tk
import tkinter.messagebox
from ui.LoginWindow import LoginWindow
from ui.ChatWindow import ChatWindow
import requests
import os

class MainWindow:
	def __init__(self,master):
		self.chat_ui = ChatWindow(master,self)
		self.login_ui = LoginWindow(master,self)
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
		self.checkLoggedIn()
	def setupMainUI(self,master):
		l1 = tk.Label(master,text="Messenger",font=("",50))
		l2  = tk.Label(master,text="Username: ",font=("",40))
		e1_text = tk.StringVar()
		e1 = tk.Entry(master,textvariable=e1_text,font=("",20))
		b1 = tk.Button(master,text="CHAT",font=("",20),command=lambda:self.chat_ui.chat(e1_text.get(),))
		b2 = tk.Button(master,text="LOGOUT",font=("",20),command=self.logout)
		self.mainWidgets = {"l1":l1,
							"l2":l2,
							"e1":e1,
							"b1":b1,
							"b2":b2}
		self.mainTextVariables = {"e1_text":e1_text}
	def showMain(self):
		self.mainWidgets["l1"].place(x=50,y=50) 
		self.mainWidgets["l2"].place(x=100,y=150) 
		self.mainWidgets["e1"].place(x=400,y=170) 
		self.mainWidgets["b1"].place(x=350,y=230) 
		self.mainWidgets["b2"].place(x=750,y=10) 

	def hideMain(self):
		for widget_name,widget_instance in self.mainWidgets.items():
			widget_instance.place_forget()
	def logout(self):
		if os.path.exists("token"):
			os.remove("token")
		else:
			print("Token not found so not deleted.")
		self.hideMain()
		self.login_ui.showLogin()
	def checkLoggedIn(self):
		@handle_requests_errors
		def func():
			try:
				with open("token") as file:
					try:
						token = file.readlines()[0]
					except IndexError:
						token = ""
					if token:
						validate_token_api = f"http://localhost:8080/api/validate_token/{token}"
						validate_token_api_res = requests.get(validate_token_api)
						json = validate_token_api_res.json()
						if json["valid_token"]:
							self.showMain()
						else:
							self.login_ui.showLogin()
					else:
						self.login_ui.showLogin()
			except FileNotFoundError:
				print("FileNotFoundError")
				self.login_ui.showLogin()
			except requests.exceptions.ConnectionError:
				print("coudn't connect to the server")
				self.login_ui.showLogin()
				tkinter.messagebox.showwarning("Connection refused","Connection refused! Please try again later.")
				self.master.destroy()