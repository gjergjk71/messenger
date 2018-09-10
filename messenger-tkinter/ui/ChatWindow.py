import tkinter as tk

class ChatWindow():
	def __init__(self,master):
		self.master = master
		self.setupChatUI(master)

	def setupChatUI(self,master):
		l1 = tk.Label(master,text="Messenger",font=("",50))

		txt_frm = tk.Frame(self.master, width=500, height=600)

		txt = tk.Text(txt_frm, borderwidth=2, relief="sunken")
		for i in range(50):
			pass
		txt.config(state="disabled")
		txt.config(font=("consolas", 12), undo=True, wrap='word')
		self.ChatWidgets = {"l1":l1,
							"txt_frm":txt_frm,
							"txt":txt}
	def showChat(self):
		self.ChatWidgets["txt_frm"].place(x=100,y=100)
		self.ChatWidgets["l1"].place(x=10,y=10)
		self.ChatWidgets["txt"].place(x=1,y=1)

	def hideChat(self):
		for widget_name,widget_instance in self.ChatWidgets.items():
			widget_instance.place_forget()
