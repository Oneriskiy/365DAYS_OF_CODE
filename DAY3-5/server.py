import websockets
import asyncio

clients = {}

async def handler(websocket):
    try:
       msg = await websocket.recv()
       if msg.startswith("__name__"):
           name = msg.split(":", 1)[1]
           clients[websocket] = name
       async for msg in websocket:
            for c, c_name in clients.items():
                if c != websocket:
                    await c.send(f"{name}, {msg}")
    except Exception:
        print("гг")
    finally:
        del clients[websocket]


async def main():
    host = 'localhost'
    port = 5000
    server = await websockets.serve(handler, host, port)
    print('сервер запущен!')
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())