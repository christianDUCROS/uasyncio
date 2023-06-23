import uasyncio
 
async def addition(a,b):
    await uasyncio.sleep(1)
    return a+b

async def soustraction(a,b):
    await uasyncio.sleep(1)
    return a-b

async def multiplication(a,b):
    await uasyncio.sleep(2)
    return a*b

async def main():
    tasks = (addition(42,45), soustraction(42,45), multiplication(42,45))
    print('synchro des retours de coroutines ...')
    res = await uasyncio.gather(*tasks)
    print(res)

uasyncio.run(main())
