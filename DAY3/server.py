import asyncio
import websockets

clients = set()

async def handler(websocket):
    clients.add(websocket)
    try:
        async for msg in websocket:
            for c in clients:
                if c != websocket:
                    await c.send(msg)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        clients.remove(websocket)

async def main():
    host = 'localhost'
    port = 5000
    server = await websockets.serve(handler, host, port)
    print('сервер запущен...')
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())