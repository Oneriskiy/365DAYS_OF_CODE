import asyncio
import websockets

clients = {}

async def handler(websocket):
    async for msg in websocket:
        if msg.startswith('__name__'):
            name = msg.split(' ')
            nickname = name[1]
            print(msg)
            clients[websocket] = name
            continue
        else:
            for c in clients:
                if c != websocket:
                    await c.send(f'{nickname}: {msg}')

async def main():
    host = 'localhost'
    port = 5000
    server = await websockets.serve(handler, host, port)
    print("server is running")
    await asyncio.Future()

asyncio.run(main())
