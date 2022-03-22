import asyncio
import websockets
import socket
import webbrowser 

# create handler for each connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = socket.gethostbyname(socket.gethostname())

HOST = 'localhost'
PORT = 3000

connected = set()

async def handler(websocket, path):
    # SERVER = socket.gethostbyname(socket.gethostname())
    # client.connect((SERVER, PORT))
    # user = await websocket.recv()
    # client.send()
    # Regiter.
    connected.add(websocket)
    try:
        # async for message in websocket:
        #     client.send(message.encode())
        #     # resp = client.recv(1024).decode()
        #     for conn in connected:
        #         if conn != websocket:
        #             await conn.send(message)
            # print(f'Resposta: {resp}')
            
        # Implement logical here
        async for message in websocket:
            print(message)
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
        
        # await asyncio.wait([ws.send('hello') for ws in connected])
        # await asyncio.sleep(10)
    finally:
        # Unregister.
        connected.remove(websocket)
        client.close()
        # print(websocket.message)

    # data = await websocket.recv()
    # print(data, path)

    # reply = f"Data recieved as:  {data}!"

    # await websocket.send(reply)

    # client.connect((HOST, PORT))



 

start_server = websockets.serve(handler, "localhost", 3333)


asyncio.get_event_loop().run_until_complete(start_server)
webbrowser.open('public/login.html')  
asyncio.get_event_loop().run_forever()
