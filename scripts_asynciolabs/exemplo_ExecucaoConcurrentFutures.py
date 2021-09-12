import asyncio
import concurrent.futures
from random import randint
from time import sleep
from functools import partial


def execProc(mod: str):
    print(f"INICIO proc mod ...: {mod}")
    sleep(randint(1,5))
    print(f"FIM proc mod ...: {mod}")

    return "OK"

lst = [1,2,3,4,5]
def gerenciaThread():
    print('Thread')
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(lst)-2) as executor:
    #with concurrent.futures.ProcessPoolExecutor(max_workers=len(lst)) as executor:
        results = executor.map(execProc, lst)

    for result in results:
        print(result)

def gerenciaProcess():
    print("Process")
    lst_submit = []
    with concurrent.futures.ProcessPoolExecutor() as executor: #sem o parametro max_workers ele calcula por qtd CPU automaticamente
        ret_1 = executor.submit(sleep, 5)
        for vlr in lst:
            lst_submit.append(executor.submit(execProc, vlr))
        print(">>", ret_1)
        ret_1.add_done_callback(partial(print, "dormi mas ja acordei !")) #qdo finaliza um submit essa funcao chama outra na sequencia !

    for worker in concurrent.futures.as_completed(lst_submit): #as_complete aguarda o final das execucoes para liberar o resultado/return
        resp = worker.result()
        print(worker, ">>>", resp)
 





if __name__ == "__main__":   
    gerenciaThread()
    gerenciaProcess()