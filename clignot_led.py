import uasyncio
from machine import Pin
pLED = Pin('LED',Pin.OUT)# RP2 W ou 25 pour RP2
 
async def blink_LED():
    while True:
        pLED.toggle() #changement état
        await uasyncio.sleep_ms(500)

async def main():
    uasyncio.create_task(blink_LED())
    #... 
    while True :
     #   ...
        await uasyncio.sleep_ms(0)

uasyncio.run(main())
