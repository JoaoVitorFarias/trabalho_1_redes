import socket
import threading

from application.tcp_server import TcpServer

class Tcp:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        

    def run(self):
        self.server_socket.listen(5)

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Cliente conectado: {client_address}")
                
            tcp_service = TcpServer(client_socket, client_address, self.server_socket)

            client_thread = threading.Thread(target=tcp_service.handle_client)
            client_thread.start()