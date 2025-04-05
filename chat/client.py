import asyncio
import websockets

SERVER_IP = "172.29.28.42"  # IP do servidor
PORT = 8765  # Porta do WebSocket

async def cliente():
    """Cliente envia e recebe mensagens com identificação."""
    uri = f"ws://{SERVER_IP}:{PORT}"

    async with websockets.connect(uri) as websocket:
        nome = input("Digite seu nome: ")  # Cliente escolhe um nome
        await websocket.send(nome)  # Envia o nome ao servidor

        print("✅ Conectado ao chat. Digite mensagens para enviar.")

        async def receber_mensagens():
            """Recebe mensagens do servidor continuamente."""
            try:
                async for resposta in websocket:
                    print(f"\n📢 {resposta}")  # Exibe mensagens recebidas no chat
            except websockets.exceptions.ConnectionClosed:
                print("❌ Conexão com o servidor encerrada.")

        asyncio.create_task(receber_mensagens())  # Inicia a tarefa de recebimento

        while True:
            mensagem = await asyncio.to_thread(input, "Digite sua mensagem: ")  # Aguarda entrada do usuário
            await websocket.send(mensagem)  # Envia a mensagem ao servidor

async def iniciar_cliente():
    """Inicia o cliente WebSocket."""
    await cliente()

if __name__ == "__main__":
    asyncio.run(iniciar_cliente())  # Executa o cliente
