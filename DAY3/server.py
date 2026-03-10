import websockets
import asyncio
from datetime import datetime as dt


def timer():
    """
    return: returns the time at the current moment
    """
    time_now = dt.now().strftime('%d.%H.%M.%S')
    return time_now

clients = set()

async def handler(websocket):
    """
    The function adds the user to the set,
    checks whether messages have arrived on the server,
    and sends them to other clients if the user has disconnected.
    It notifies them of this.
    """
    clients.add(websocket)
    print(f"{timer()} | the user has connected")
    try:
        async for msg in websocket:
            for c in clients:
                if c != websocket:
                    await c.send(msg)
    except Exception:
        print(f"{timer()} | user disconnected")
    finally:
        clients.remove(websocket)


async def main():
    """
    The main function starts the server on the local host
    and runs the handler() function.
    """
    host = 'localhost'
    port = 5000
    server = await websockets.serve(handler, host, port)
    print(f'{timer()} | server is running')
    await asyncio.Future()

asyncio.run(main())