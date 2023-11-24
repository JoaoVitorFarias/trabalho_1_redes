import json

from application.operation_service import OperationService

class TcpServer:
    def __init__(self, client_socket, client_address, server_socket):
        self.client_socket = client_socket
        self.client_address = client_address
        self.server_socket = server_socket

    def handle_client(self):
        operation = OperationService()
        while True:
            data = self.client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            message = json.loads(data)

            if message['operation'] == 'add':
                self.send_result(operation.add(message['arg1'], message['arg2']))

            elif message['operation'] == 'sub':
                self.send_result(operation.sub(message['arg1'], message['arg2']))
            
            elif message['operation'] == 'mul':
                self.send_result(operation.mul(message['arg1'], message['arg2']))

            elif message['operation'] == 'div':
                self.send_result(operation.div(message['arg1'], message['arg2']))

            else:
                response = {"error": "invalid_option"}
                data = json.dumps(response)
                self.client_socket.sendall(bytes(data,encoding="utf-8"))

    def send_result(self, result):
        response = {"result": result}
        data = json.dumps(response)
        self.client_socket.sendall(bytes(data,encoding="utf-8"))

    def close(self):
        self.client_socket.close()
        self.server_socket.close()