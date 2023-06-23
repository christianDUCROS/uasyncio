#programme principal lance une coroutine (print_word() )
#constat : hello est imprimé avant word !!!!!
import uasyncio
import time

async def print_hello():
    print('hello')

async def print_word():
    print('word')
    await uasyncio.sleep_ms(3000)
    print('word2')

#main
while True : 
    uasyncio.create_task(print_hello())
    uasyncio.run(print_word())
    print('Bonjour')
    time.sleep_ms(1000)
    print('Christian')

'''
# même programme mais erreur sur main placé dans la pile
import uasyncio

async def print_hello():
    print('hello')

async def print_word():
    print('word')
    await uasyncio.sleep_ms(3000)
    print('word2')

async def main():
    while True : 
        uasyncio.create_task(print_hello())
        uasyncio.run(print_word())
        print('Bonjour')
        await uasyncio.sleep_ms(1000)
        print('Christian')

uasyncio.run(main())
'''