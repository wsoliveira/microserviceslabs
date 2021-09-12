## Scripts
 - exemplo_aioHttp.py - Executa 2 GET's de forma assincrona usando asyncio, aiohttp e aiofiles
 - exemplo_ExecucaoConcurrentFutures.py -  Realiza execuções paralelas usando a classe concurrent com as funcoes Process e Threads
 - exemplo_gravandoArquivo.py - Script simples fazendo testes de gravação de dados em arquivo de forma assincrona
 - exemplo_vendedorDeBala.py - Classico Teste do famoso exemplo de vendedor de bala que empacota balas e vende no balcao (um pessoa/tarefa com duas funções que não pode ter concorrencia)

## Gerar Imagem Docker
docker build -t asynciolabs .

# Para rodar os scripts
docker run -it asynciolabs exemplo_aioHttp.py
docker run -it asynciolabs exemplo_ExecucaoConcurrentFutures.py
docker run -it asynciolabs exemplo_gravandoArquivo.py
docker run -it asynciolabs exemplo_vendedorDeBala.py


## Subir Imagem para o HUB
docker login --username wsoliveiraudia
docker tag asynciolabs wsoliveiraudia/asynciolabs
docker push wsoliveiraudia/asynciolabs