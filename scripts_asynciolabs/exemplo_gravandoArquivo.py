import asyncio
from aiofiles import open as aopen


async def write_file(n: str):    
    async with aopen('teste.txt', 'a') as f:
        print(n)
        await f.write(f'{n}\n')


async def run():
    tasks = []
    for n in range(1, 11):
        task = asyncio.ensure_future(write_file(n))
        tasks.append(task)

    results = asyncio.gather(*tasks) #rodando todas
    await results #e aguardando a execucao de todas

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)