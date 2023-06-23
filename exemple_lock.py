import uasyncio
import utime

async def task1():
    await lock1.acquire()
    print("Acquired lock in task1", utime.ticks_ms())
    utime.sleep_ms(100)
    await uasyncio.sleep_ms(400)
    lock1.release()

async def task2():
    await lock1.acquire()
    print("Acquired lock in task2", utime.ticks_ms())
    utime.sleep_ms(200)
    await uasyncio.sleep_ms(800)
    lock1.release()


async def main():
    while  True : 
        uasyncio.create_task(task1())
        uasyncio.create_task(task2())
        await uasyncio.sleep_ms(1000)
        
        
lock1 = uasyncio.Lock()  # The Lock instance
lock2 = uasyncio.Lock()  # The Lock instance

uasyncio.run(main())  # Run for 10s