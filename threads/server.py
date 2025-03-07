import socket
import json
import threading

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

clients = {}

print(f"Servidor ouvindo em {HOST}:{PORT}...")

def handle_client(conn, addr):
    ip_client, port_client = addr

    try:
        while True:
            data = conn.recv(1024).decode()
            
            if not data:
                break

            try:
                msg_dict = json.loads(data)
                client_id = msg_dict.get("id", "Id desconhecido")
                nome = msg_dict
                msg = msg_dict.get("msg", "Mensagem não encontrada")

                clients[client_id] = {"nome": nome, "msg": msg}

                print(f"Cliente {nome}: {msg}")

                response = {
                    "status": "Mensagem recebida",
                    "client_id": client_id,
                    "clientes_conectados": list(clients.values())
                }
                conn.sendall(json.dumps(response).encode())
            
            except:
                conn.sendall(json.dumps({"erro": "Formato inválido"}).encode())

    except:
        print(f"Cliente {nome}:{port_client} desconectou.")
    
    finally:
        conn.close()
        clients.pop(client_id, None)
        print(f"Cliente {ip_client}:{port_client} removido.")

while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()