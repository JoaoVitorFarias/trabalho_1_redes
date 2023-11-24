from dotenv import load_dotenv
import os
import tkinter as tk

from presentation.socket.tcp import Tcp

load_dotenv()

SERVER_HOST = os.getenv('HOST')
SERVER_PORT = int(os.getenv('PORT'))

root = tk.Tk()
server = Tcp(SERVER_HOST, SERVER_PORT, root)
server.run()


