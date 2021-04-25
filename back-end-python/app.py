import asyncio
import websockets

connected = set()

PORT = 5000
HOST = "0.0.0.0"

async def server(websocket, path):
    connected.add(websocket)
    print("connection!")
    try:
        async for message in websocket:
            for conn in connected:
                print(message)
                await conn.send(message)
    finally:
        connected.remove(websocket)


start_server = websockets.serve(server, HOST, PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

 
