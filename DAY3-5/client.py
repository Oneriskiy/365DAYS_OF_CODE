import websockets
import asyncio


async def listen(websocket):
    async for msg in websocket:
        print(msg)


async def send(websocket):
    loop = asyncio.get_running_loop()
    while True:
       msg =  loop.run_in_executor(None, input)
       await websocket.send(msg)


async def main():
    async with websockets.connect('ws://localhost:5000') as websocket:
        name = input("Введите имя: ")
        await websocket.send(f"__name__:{name}")
        await asyncio.gather(listen(websocket), send(websocket))

if __name__ == "__main__":
    asyncio.run(main())