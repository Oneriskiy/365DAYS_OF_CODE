import asyncio
import websockets

async def listen(websocket):
    """
    Checks for incoming messages,
    if found, immediately displays them to the client
    """
    async for msg in websocket:
        print(f"sent to you: {msg}")

async def send(websocket):
    """
    asks the user for a message and sends it to another client
    """
    while True:
        loop = asyncio.get_running_loop()
        msg = await loop.run_in_executor(None, input)
        await websocket.send(msg)

async def main():
    """
    The main function connects the client to the server
    and activates other functions (listen(), send())
    """
    async with websockets.connect('ws://localhost:5000') as websocket:
        await asyncio.gather(listen(websocket),send(websocket))