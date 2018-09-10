import tkinter as tk
import requests

class ChatWindow():
	def __init__(self,master):
		self.master = master
		self.setupChatUI(master)

	def setupChatUI(self,master):
		l1 = tk.Label(master,text="Messenger",font=("",50))

		txt_frm = tk.Frame(self.master, width=750, height=600)

		txt = tk.Text(txt_frm, borderwidth=2, relief="sunken")
		txt.config(state="disabled")
		txt.config(font=("consolas", 12), undo=True, wrap='word')
		self.ChatWidgets = {"l1":l1,
							"txt_frm":txt_frm,
							"txt":txt}
	def showChat(self,receiver):
		self.ChatWidgets["txt_frm"].place(x=100,y=100)
		self.ChatWidgets["l1"].place(x=10,y=10)
		self.ChatWidgets["txt"].place(x=1,y=1)
		self.updateMessages(receiver)

	def updateMessages(self,receiver):
		try:
			with open("token") as file:
				token = file.readlines()[0]
				conversation_api = "http://localhost:8080/api/{}/chat/{}".format(token,receiver)
			print(conversation_api)
			response = requests.get(conversation_api)
			json = response.json()

			self.ChatWidgets["txt"].config(state="normal")
			self.ChatWidgets["txt"].delete("1.0",tk.END)
			for message in json["messages"]:
				self.ChatWidgets["txt"].insert(tk.END,f"[{message[0]}] ({message[2]}) - {message[1]}\n")
			self.ChatWidgets["txt"].config(state="disabled")	
			print("Messages updated")
		except requests.exceptions.ConnectionError:
			print("Failed to establish a new connection: [Errno 111] Connection refused',))")
		self.master.after(1000,lambda:self.updateMessages(receiver=receiver))	

	def hideChat(self):
		for widget_name,widget_instance in self.ChatWidgets.items():
			widget_instance.place_forget()