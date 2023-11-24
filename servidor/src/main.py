from dotenv import load_dotenv
import os
import socket

from presentation.socket.tcp import Tcp

load_dotenv()

PORT = int(os.getenv('PORT'))
HOST = socket.gethostname()
ip_address = socket.gethostbyname(HOST)
print(f"Nome do computador: {HOST}")
print(f"Endereco IP: {ip_address}")

server = Tcp(HOST, PORT)
server.run()