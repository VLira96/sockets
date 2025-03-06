import socket
import json
import uuid

client_id = uuid.uuid4()


HOST = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

msg_dict = {
    "id": f"{client_id}",
    "nome": "Jão",
    "msg": "Q fase tá o curintia"
}

client_socket.sendall(json.dumps(msg_dict).encode())

print(json.loads(client_socket.recv(1024).decode()))
client_socket.close()