import asyncio
import websockets
import multiprocessing

SERVER_IP = "172.29.28.42"  # IP do servidor
PORT = 8765  # Porta do WebSocket
clientes_conectados = {}  # Dicionário que armazena {websocket: nome}

async def servidor(websocket):
    """Gerencia conexões de clientes e faz broadcast das mensagens identificadas."""
    try:
        # Primeira mensagem deve ser o nome do cliente
        nome = await websocket.recv()
        clientes_conectados[websocket] = nome
        print(f"🔵 {nome} conectou ao chat!")

        async for mensagem in websocket:
            remetente = clientes_conectados.get(websocket, "Desconhecido")
            print(f"📩 Mensagem de {remetente}: {mensagem}")
            
            mensagem_formatada = f"{remetente}: {mensagem}"

            # Envia a mensagem formatada para todos os clientes conectados
            await asyncio.gather(
                *[cliente.send(mensagem_formatada) for cliente in clientes_conectados if cliente != websocket]
            )
    
    except websockets.exceptions.ConnectionClosed:
        print(f"🔴 {clientes_conectados.get(websocket, 'Desconhecido')} desconectou.")
    finally:
        clientes_conectados.pop(websocket, None)  # Remove cliente ao desconectar

async def iniciar_servidor():
    """Inicia o servidor WebSocket."""
    async with websockets.serve(servidor, SERVER_IP, PORT):
        print(f"✅ Servidor rodando em ws://{SERVER_IP}:{PORT}")
        await asyncio.Future()  # Mantém o servidor rodando

def iniciar_servidor_processo():
    asyncio.run(iniciar_servidor())

if __name__ == "__main__":
    processo_servidor = multiprocessing.Process(target=iniciar_servidor_processo)
    processo_servidor.start()
    processo_servidor.join()
