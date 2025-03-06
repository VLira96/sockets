import socket
import json

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Servidor escutando em {HOST}:{PORT}")

while True:

    conn, [ip_cliente, porta_cliente] = server_socket.accept()
    print(f"Conexão recebida de {ip_cliente}:{porta_cliente}")

    data = conn.recv(1024).decode()

    if not data:
        print("Json vazio. Fim da comunicação!")
        break

    try:
        msg_dict = json.loads(data)
        nome = msg_dict.get("nome", "Nome não encontrado!")
        msg = msg_dict.get("msg", "Mensagem não encontrada!")

        print(f"Cliente {nome} {ip_cliente}:{porta_cliente} {msg}")

        conn.sendall(json.dumps({"resposta": "Mensagem recebida!", "cliente": f"{ip_cliente}: {porta_cliente}"}).encode())    

    except:
        print("Erro na decodificação do JSON.")
        conn.sendall(json.dumps({"resposta": "Formato inválido!"}).encode())

    
    conn.close()