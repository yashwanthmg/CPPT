import websockets
import asyncio
import json


async def main():
    uri = "wss://www.bitmex.com/realtime"
    async with websockets.connect(uri) as websocket:
        # Send a message to subscribe to XBTUSD updates
        msg = {
            "op": "subscribe",
            "args": ["instrument:XBTUSD"]
        }
        await websocket.send(json.dumps(msg))

        # Receive messages in a loop and print them out
        while True:
            result = await websocket.recv()
            data = json.loads(result)
            print(data)


if __name__ == "__main__":
    # Run the 'main' function in an asyncio event loop
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
