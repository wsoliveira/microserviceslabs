#https://medium.com/@edytarcio/async-await-introdu%C3%A7%C3%A3o-%C3%A0-programa%C3%A7%C3%A3o-ass%C3%ADncrona-em-python-fa30d077018e

import asyncio
import time
import random
from  aiofiles  import open as aiopen

async def vendedorAtendeBalcao():
    if random.randint(1,5)//2:
        print("Inicio atendimento balcao")
        #time.sleep(random.randint(1,5))
        print("Fim atendimento balcao")
        return True
    else:
        return False


async def vendedorEmpacotaBala():
    print("Empacotando bala")
    result = await vendedorAtendeBalcao() #asyncio.sleep(0.1)
    if result:
        print("voltando a empacotar bala")    

loop = asyncio.get_event_loop()

#tasks = [loop.create_task(vendedorEmpacotaBala()),
#         loop.create_task(vendedorAtendeBalcao())]

#wait_tasks = asyncio.wait(tasks)
#loop.run_until_complete(wait_tasks)
#loop.close()

loop.run_until_complete(vendedorEmpacotaBala())
loop.close()

#task = asyncio.ensure_future(vendedorEmpacotaBala())
#loop.run_forever()  ###DAEMON ###loop.stop() para parar a execucao

