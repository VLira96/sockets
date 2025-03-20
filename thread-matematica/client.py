import socket

HOST = '127.0.0.1'
PORT = 12345

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((HOST, PORT))

def enviar_conta(conta):
    socket_client.send(conta.encode())
    print(f"Resultado: {socket_client.recv(1024).decode()}")
    socket_client.close()

conta = input("Digite uma conta matemática: ")
enviar_conta(conta)