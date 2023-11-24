import json
import re
import socket

class TcpServer:
    def __init__(self, client_socket):
        self.client_socket = client_socket

    def calculate(self, expression):
        matches = re.findall(r'(\d+|\S)', expression)
        values = [int(match) if match.isdigit() else match for match in matches]
        result=values[0]

        for i in range(1, len(values), 2):
            operator = values[i]
            value = values[i + 1]

            if operator == '+':
                result = self.handle_with_operation(result, value, 'add')
            elif operator == '-':
                result = self.handle_with_operation(result, value, 'sub')
            elif operator == '*':
                result = self.handle_with_operation(result, value, 'mul')
            elif operator == '/':
                result = self.handle_with_operation(result, value, 'div')
        
        return result
    
    def handle_with_operation(self, arg1, arg2, operation):
        try:
            self.send_message(arg1, arg2, operation)
        except socket.timeout:
            self.send_message(arg1, arg2, operation)
    
        return self.receive_message()


    def send_message(self, arg1, arg2, operation):
        self.client_socket.settimeout(10)
        message = {"operation": operation, "arg1": arg1, "arg2": arg2}        
        data = json.dumps(message)
        self.client_socket.send(data.encode('utf-8'))

    def receive_message(self):
        response = self.client_socket.recv(1042).decode('utf-8')
        if not response:
            return None
        response_json = json.loads(response)

        return response_json['result']

