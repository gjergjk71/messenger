from requests.exceptions import RequestException
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError
from requests.exceptions import TooManyRedirects
import tkinter.messagebox

def handle_requests_errors(func):
	try:
		func()
	except ConnectionError as e:
		tkinter.messagebox.showwarning("Connection refused","Connection refused! Please try again later.")
	except:
		tk.messagebox.showwarning("Something unexpected happened! Please try again later.")