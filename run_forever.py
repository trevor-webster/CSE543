import asyncio

loop = asyncio.get_event_loop()

async def flood_arp():
    n = 0
    while True:
        print(f"{n}")
        await asyncio.sleep(2)
        n = n+1

async def listen_reply():
    while True:
        await asyncio.sleep(5)
        print("listen reply")

def main():
    future1 = loop.create_task(flood_arp())
    future2 = loop.create_task(listen_reply())

    try:
        loop.run_forever()
    finally:
        loop.stop()


main()