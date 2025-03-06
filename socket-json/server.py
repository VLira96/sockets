import socket
import json

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Servidor ouvindo em {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    # print(f"Conexão recebida de {addr}")

    data = conn.recv(1024).decode()

    if not data:
        break

    try:
        msg_dict = json.loads(data)
        nome = msg_dict.get("nome", "Não identificado")
        msg = msg_dict.get("msg", "Problemas ao receber a mensagem")
        print(f"{nome}: {msg}")

        response = {"status": "Mensagem recebida", "servidor": "Deu foi bom!"}
        conn.sendall(json.dumps(response).encode())

    except:
        print("Erro na decodificação do json!")
        conn.sendall(json.dumps({"erro": "Formato inválido"}).encode())

    conn.close()