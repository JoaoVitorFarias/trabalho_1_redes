import tkinter as tk

from application.tcp_server import TcpServer

class Screen():
    def __init__(self, root, client_socket) -> None:
        self.client_socket = client_socket
        self.root = root
        self.tcp_server = TcpServer(client_socket)
        self.root.title("Calculadora")
        self.root.geometry("300x400")

        self.result_var = tk.StringVar()

        entry = tk.Entry(self.root, textvariable=self.result_var, font=('Helvetica', 16), justify='right')
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.root, text=text, command=lambda t=text: self.handle_button(t), font=('Helvetica', 16))
            button.grid(row=row, column=column, sticky='nsew')
        
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)


    def handle_button(self, text):
        if text == '=':
            try:
                result = self.tcp_server.calculate(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Erro")
        elif text == 'C':
            self.result_var.set('')
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + text)

