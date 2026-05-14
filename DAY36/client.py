import asyncio
import websockets
from messenger_window import *

async def send(websocket):
        if text.text():
            success.setText('Отправлено!')
            await websocket.send(text.text())
        else:
            success.setText('Введите текст!')
        success.show()
        await asyncio.sleep(2)
        success.hide()

async def listen(websocket):
    async for msg in websocket:
        chat.append(f'{msg}')


def send_message():
    asyncio.create_task(send(websocket_gl))

button.clicked.connect(send_message)

async def main():
    URI = "ws://localhost:5000"
    window.show()
    async with websockets.connect(URI) as websocket:
        name = input('input the nickname: ')
        await websocket.send(f"__name__ {name}")
        global websocket_gl
        websocket_gl = websocket
        print("client is running")
        asyncio.create_task(
            listen(websocket)
        )
        while True:
            app.processEvents()
            await asyncio.sleep(0.01)

asyncio.run(main())

