
import uasyncio
import utime

async def task1 ():
    print("T1 en cours", utime.ticks_ms())
    await uasyncio.sleep_ms(1500)
    print("fin tache 1", utime.ticks_ms())


async def main():   
    tache_1 = uasyncio.create_task(task1())
    print('main : ',utime.ticks_ms())
    await uasyncio.sleep(0) #lancement de task1
    tache_1.cancel()
    await uasyncio.sleep_ms(2000) #lancement de task1
    print('main après cancel : ',utime.ticks_ms())
    
    
event = uasyncio.Event()
uasyncio.run(main())
