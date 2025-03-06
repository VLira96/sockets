import socket
import json

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

msg_dict = {
    'nome': "Joaquim",
    'msg': "Salve pae!"
}

client_socket.sendall(json.dumps(msg_dict).encode())

response = client_socket.recv(1024).decode()
response_dict = json.loads(response)
print(f"Resposta do servidor: {response_dict}")