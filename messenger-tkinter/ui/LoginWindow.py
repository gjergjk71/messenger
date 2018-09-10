import tkinter as tk
import requests

class LoginWindow():
	def __init__(self,master):
		self.setupLoginUI(master)
	def setupLoginUI(self,master):
		l1 = tk.Label(master,text="Sign in",font=("",50))

		l2 = tk.Label(master,text="Username: ",font=("",30))

		e1_text = tk.StringVar()
		e1 = tk.Entry(master,textvariable=e1_text,font=("",20))
		e1.bind("<Return>", self.login)

		l3 = tk.Label(master,text="Password:",font=("",30))

		e2_text = tk.StringVar()
		e2 = tk.Entry(master,textvariable=e2_text,font=("",20),show="*")
		e2.bind("<Return>", self.login)

		l4 = tk.Label(master,text="Username or Password is wrong!",font=("",20))

		b1 = tk.Button(master,text="Login",font=("",28),command=self.login)
		b2 = tk.Button(master,text="Register",font=("",28))
		self.loginWidgets = {
				"label1":l1,
				"label2":l2,
				"label3":l3,
				"label4":l4,
				"entry1":e1,
				"entry2":e2,
				"button1":b1,
				"button2":b2}
		self.loginTextVariables = {"e1_text":e1_text,
								   "e2_text":e2_text}
	def showLogin(self):
		self.loginWidgets["label1"].place(x=30,y=30) # Sign in
		self.loginWidgets["label2"].place(x=130,y=180) # Username 
		self.loginWidgets["label3"].place(x=135,y=250) # Password 

		self.loginTextVariables["e1_text"].set("")
		self.loginTextVariables["e2_text"].set("")
		self.loginWidgets["entry1"].place(x=360,y=180,width=300,height=55) # Entry for username
		self.loginWidgets["entry2"].place(x=360,y=250,width=300,height=55) # Entry for password

		self.loginWidgets["button1"].place(x=300,y=330,width=150,height=50) # Button for login 
		self.loginWidgets["button2"].place(x=470,y=330,width=160,height=50) # Button for show register
	def hideLogin(self):
		print(self.loginWidgets)
		for widget_name,widget_instance in self.loginWidgets.items():
			print(widget_name)
			widget_instance.place_forget()
	def login(self):
		pass #Overwrotted in MainWindow.py