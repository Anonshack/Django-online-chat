import asyncio
import websockets
connected = set()


async def chat_handler(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            for user in connected:
                if user != websocket:
                    await user.send(message)
    except Exception:
        pass
    finally:
        connected.remove(websocket)

start_server = websockets.serve(chat_handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
