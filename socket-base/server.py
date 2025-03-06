import socket

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Servidor ouvindo em {HOST}:{PORT}...")

while True:
    conn, addr = server_socket.accept()
    print(f"Conexção recebida de {addr}")

    mensagem = conn.recv(1024).decode()
    print(f"Cliente: {mensagem}")

    respota = "Mensagem recebida no servidor!"
    conn.sendall(respota.encode())

    conn.close