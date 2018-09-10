import tkinter as tk

class ChatWindow():
	def __init__(self,master):
		self.master = master
		self.setupChatUI(master)
	def setupChatUI(self,master):
		l1 = tk.Label(master,text="Messenger",font=("",50))

		txt_frm = tk.Frame(self.master, width=600, height=600)

		txt = tk.Text(txt_frm, borderwidth=3, relief="sunken")
		for i in range(50):
			txt.insert(tk.END,"DSADASD\n")
		txt.config(state="disabled")
		txt.config(font=("consolas", 12), undo=True, wrap='word')
		scrollb = tk.Scrollbar(txt_frm, command=txt.yview)
		txt['yscrollcommand'] = scrollb.set
		self.ChatWidgets = {"l1":l1,
							"txt_frm":txt_frm,
							"txt":txt,
							"scrollb":scrollb}
	def showChat(self):
		self.ChatWidgets["txt_frm"].place(x=50,y=50)
		self.ChatWidgets["l1"].place(x=60,y=60)
		self.ChatWidgets["scrollb"].place(x=100,y=100)
		self.ChatWidgets["txt"].place(x=100,y=100)

	def hideChat(self):
		for widget_name,widget_instance in self.ChatWidgets.items():
			widget_instance.place_forget()
