import uasyncio
import utime

async def task1 ():
    print("T1 attend event ", utime.ticks_ms())
    await event.wait()
    event.clear()  # Flag caller and enable re-use of the event
    print("L'événement est passé", utime.ticks_ms())

async def task2 ():
    print("T2 attend event ", utime.ticks_ms())
    await event.wait()
    event.clear()  # Flag caller and enable re-use of the event
    print("L'événement est passé", utime.ticks_ms())
  



async def main():   
    uasyncio.create_task(task1())
    uasyncio.create_task(task2())
    print('main avant event: ',utime.ticks_ms())
    await uasyncio.sleep(2)
    print('Setting event')
    event.set()
    await uasyncio.sleep(2)
    
event = uasyncio.Event()
uasyncio.run(main())