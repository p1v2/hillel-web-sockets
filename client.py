import asyncio
import websockets


async def connect_websocket():
    uri = "ws://localhost:8000/ws/chat/lobby/"  # Replace with the WebSocket server URI

    async with websockets.connect(uri) as websocket:
        while True:
            # message = input("Enter a message to send (or 'exit' to quit): ")
            #
            # if message == "exit":
            #     break
            #
            # await websocket.send(message)
            # print("Message sent:", message)

            response = await websocket.recv()
            print("Received:", response)


asyncio.get_event_loop().run_until_complete(connect_websocket())