import asyncio
from os.path import exists
from os import makedirs
from shutil import rmtree
from urllib.parse import urljoin
from aiohttp import ClientSession
from aiofiles import open as aopen
from requests import get

path = 'downloads'
base_url = 'https://pokeapi.co/api/v2/'
pokemons = get(urljoin(base_url, 'pokemon/?limit=10')).json()['results']

if exists(path):
    rmtree(path)
makedirs(path)


async def write_file(session, url, name):
    async with session.get(url) as response:
        print(f'baixando {name}: {url.split(".")[-2]}')
        async with aopen(f'{path}/{name}.jpg', 'wb') as f:
            content = await response.content.read()
            await f.write(content)


async def fetch(sem, session, url, name):
    async with sem:
        async with session.get(url) as response:
            result = await response.json()
            sprite_url = result['sprites']['front_default']
            await write_file(session, sprite_url, name)

async def main():
    tasks = []
    sem = asyncio.Semaphore(5) #Semaforo para controlar a concorrencia, ja tem implantando acquire, lock e release

    async with ClientSession() as session:
        for pokemon in pokemons:
            url = pokemon['url']
            name = pokemon['name']
            print(name, url)
            task = asyncio.ensure_future(fetch(sem, session, url, name)) #criando a task
            tasks.append(task)
        responses = asyncio.gather(*tasks) #liberando execucao com concorrencia entre as tasks
        await responses #aguardando todas as execucoes das tasks


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(main())   #similar ao asyncio.create_task, porem, o ensure_future ja tem o createTask encapsulado e achei mais simples trabalhar com retorno futuro do ensure
loop.run_until_complete(future) #Roda ate completar