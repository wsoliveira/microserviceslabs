## Para rodar o app
uvicorn main:app --port 8010 --reload

## Gerar Imagem Docker
docker build -t cadastro .
# Para rodar o container criado
docker run -d --name applabs_cadastro -p 8010:8010 cadastro

## Subir Imagem para o HUB
docker login --username wsoliveiraudia
docker tag cadastro wsoliveiraudia/appcadastro_labs
docker push wsoliveiraudia/appcadastro_labs