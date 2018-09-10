import tkinter as tk
from ui.MainWindow import MainWindow
from ui.LoginWindow import LoginWindow

if __name__ == "__main__":
	root = tk.Tk()
	MainWindow(root)
	root.mainloop()