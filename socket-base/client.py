import socket

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

mensagem = "funciona haha"
client_socket.sendall(mensagem.encode())

resposta = client_socket.recv(1024).decode()
print(f"Servidor: {resposta}")

client_socket.close