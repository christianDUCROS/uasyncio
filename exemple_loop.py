import uasyncio

async def task1():
    print("task1 en cours")
    await uasyncio.sleep(1)

async def task2():
    print("task2 en cours")
    await uasyncio.sleep(2)

async def main():
    while True:
        await task1()
        await task2()

loop = uasyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
