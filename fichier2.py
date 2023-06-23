
#programmation de plusieurs tâches
import uasyncio

async def print_hello():
    print('hello')

async def print_word():
    print('word')

async def main():
    while True : 
        uasyncio.create_task(print_hello())
        uasyncio.create_task(print_word())
        print('Bonjour')
        await uasyncio.sleep_ms(1000) # lancement des tâches programmées et attente de 1s
        print('Christian')

uasyncio.run(main())

'''
#même exmpel avec 
#lancement immédiat de print_hello()
import uasyncio

async def print_hello():
    print('hello')

async def print_word():
    print('word')

async def main():
    while True : 
        uasyncio.create_task(print_hello())
        await uasyncio.sleep_ms(0)
        uasyncio.create_task(print_word())
        print('Bonjour')
        await uasyncio.sleep_ms(1000) # lancement des tâches programmées et attente de 1s
        print('Christian')

uasyncio.run(main())
'''
'''
#programmation de plusieurs tâches
# changement de la coroutine "mère" et sa conséquence ( abandon de la coroutine main()  
import uasyncio

async def print_hello():
    print('hello')

async def print_word():
    print('word')

async def main():
    while True : 
        uasyncio.create_task(print_hello())
        uasyncio.run(print_word())
        print('Bonjour')
        await uasyncio.sleep_ms(1000) # lancement des tâches programmées et attente de 1s
        print('Christian')

uasyncio.run(main())
'''