import threading
import socket
from calculadora import calculadora

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Servidor ouvindo em {HOST}:{PORT}...")

def handle_client(conn, addr):
    print(f"Conexão com {addr} estabelecida.")
    while True:
        data = conn.recv(1024)
        if not data:
            break

        conta = data.decode()
        resultado = calculadora(conta)
        conn.send(str(resultado).encode())
    conn.close()
    print(f"Conexão com {addr} encerrada.")

while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()