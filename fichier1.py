#programmation asynchrone
import uasyncio

async def co_main():
    while True :
        print('hello')
        print('world')
        await uasyncio.sleep_ms(1000)

#main
uasyncio.run(co_main())
print('Salut')

'''
#programmation synchrone
import utime 

def co_main ():
    while True :
        print('hello')
        print('world')
        utime.sleep_ms(1000)

#main
co_main()
print('Salut')
'''