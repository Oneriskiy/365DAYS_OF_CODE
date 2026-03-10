import websockets
import asyncio
from datetime import datetime as dt
from config import logger


def timer():
    """
    return: returns the time at the current moment
    """
    time_now = dt.now().strftime("%d.%H.%M.%S")
    return time_now


clients = {}


async def handler(websocket):
    """
    The function adds the user to the set,
    checks whether messages have arrived on the server,
    and sends them to other clients if the user has disconnected.
    It notifies them of this.
    """
    try:
        msg = await websocket.recv()
        if msg.startswith("__name__:"):
            name = msg.split(":", 1)[1]
            clients[websocket] = name
            logger.debug(f"{name} the user has connected")
        async for msg in websocket:
            for c, c_name in clients.items():
                if c != websocket:
                    await c.send(f"{name}: {msg}")
    except Exception:
        logger.info("user disconnected")
    finally:
        del clients[websocket]


async def main():
    """
    The main function starts the server on the local host
    and runs the handler() function.
    """
    host = "localhost"
    port = 5000
    server = await websockets.serve(handler, host, port)
    print(f"{timer()} | server is running")
    logger.debug("server is running")
    await asyncio.Future()


asyncio.run(main())
