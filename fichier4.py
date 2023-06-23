import uasyncio

async def print_hello():
    print('hello')

async def print_word():
    print('word')

async def co_main():
    uasyncio.create_task(print_hello())
    uasyncio.create_task(print_word())
    await uasyncio.sleep_ms(0)

#main
print('Bonjour')
uasyncio.run(co_main())
print('Christian')
