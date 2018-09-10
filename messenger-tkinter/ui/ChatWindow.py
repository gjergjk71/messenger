import tkinter as tk

class ChatWindow():
	def __init__(self,master):
		self.master = master
		self.setupChatUI(master)
	def setupChatUI(self,master):
		l1 = tk.Label(master,text="Messenger",font=("",50))

        txt_frm = tk.Frame(self.root, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        txt_frm.grid_propagate(False)

        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

        self.txt = tk.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        scrollb = tk.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.place(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set
		self.ChatWidgets = {"l1":l1,
							"t1":t1}
	def showChat(self):
		self.ChatWidgets["t1"].place(x=50,y=50)
		self.ChatWidgets["t1"].place(x=10,y=10)
	def hideChat(self):
		for widget_name,widget_instance in self.ChatWidgets.items():
			widget_instance.place_forget()
