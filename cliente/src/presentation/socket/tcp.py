import socket
from presentation.socket.screen import Screen

class Tcp:
    def __init__(self, host, port, root):
        self.host = host
        self.port = port
        self.root = root

    def run(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        Screen(self.root, client_socket)
        self.root.mainloop()