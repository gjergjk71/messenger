import tkinter as tk
import requests

class ChatWindow():
	def __init__(self,master):
		self.master = master
		self.setupChatUI(master)
		self.current_conversation_id = None

	def setupChatUI(self,master):
		l1 = tk.Label(master,text="Messenger",font=("",50))

		txt_frm = tk.Frame(self.master, width=750, height=400)

		txt = tk.Text(txt_frm, borderwidth=2, relief="sunken")
		txt.config(state="disabled")
		txt.config(font=("consolas", 12), undo=True, wrap='word')
		txt2 = tk.Text(master,width=60,height=2)
		txt2.config(font=("consolas", 12), undo=True, wrap='word')
		txt2.bind("<Return>",lambda x:self.sendMessage(content=txt2.get("1.0",tk.END)))
		b1 = tk.Button(master,width=20,height=2,text="SEND",command=lambda:self.sendMessage(content=txt2.get("1.0",tk.END)))
		self.ChatWidgets = {"l1":l1,
							"txt_frm":txt_frm,
							"txt":txt,
							"txt2":txt2,
							"b1":b1}
	def showChat(self,receiver):
		self.ChatWidgets["txt_frm"].place(x=100,y=100)
		self.ChatWidgets["l1"].place(x=10,y=10)
		self.ChatWidgets["txt"].place(x=1,y=1)
		self.ChatWidgets["txt2"].place(x=80,y=510)
		self.ChatWidgets["b1"].place(x=700,y=510)
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
			for message in reversed(json["messages"]):
				self.ChatWidgets["txt"].insert(tk.END,f"[{message[0]}] ({message[2]}) - {message[1]}\n")
			self.ChatWidgets["txt"].config(state="disabled")	
			print("Messages updated")
		except requests.exceptions.ConnectionError:
			print("Failed to establish a new connection: [Errno 111] Connection refused',))")
		self.master.after(1000,lambda:self.updateMessages(receiver=receiver))	

	def hideChat(self):
		for widget_name,widget_instance in self.ChatWidgets.items():
			widget_instance.place_forget()

	def sendMessage(self,content):
		#self.ChatWidgets["txt"].xview("end")
		print(content)
		self.ChatWidgets["txt2"].delete("1.0",tk.END)
		#try:
		with open("token") as file:
			token = file.readlines()[0]
			send_message_api = "http://localhost:8080/api/{}/create_message/{}".format(token,self.current_conversation_id)
		response = requests.post(send_message_api,data={"content":content})
		print(response.json())
		#except:
		#	print("something unexcepted happened")