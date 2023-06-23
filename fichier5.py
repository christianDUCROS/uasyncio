##test synchro avec print_hello_word
import uasyncio
 
async def print_hello_word():
    print('hello')
    await uasyncio.sleep(2)
    print('word')
    return ('hello word')

async def main():
    # code de la fonction main
    task  = uasyncio.create_task(print_hello_word())
    await uasyncio.sleep(0)  # permet de lancer la fonction s’il y a du code dans main
    # code de la fonction main
    retour = await task
   # code de la fonction main    
    print(retour)
    
uasyncio.run(main())
