## rodar o projeto

set ou export FLASK_ENV=Development
set ou export FLASK_DEBUG=True
flask db init
flask db migrate
flask db upgrade
flask run ou python app.py


## Para rodar o celery
celery -A tasks.tasks.app_celery flower --port=5566
celery -A tasks.tasks.app_celery worker  --loglevel=info

## Gerar Imagem Docker
docker build -t recurso .
# Para rodar o container criado
docker run -d --name applabs_recurso -p 8020:8020 recurso

## Subir Imagem para o HUB
docker login --username wsoliveiraudia
docker tag recurso wsoliveiraudia/apprecurso_labs
docker push wsoliveiraudia/apprecurso_labs