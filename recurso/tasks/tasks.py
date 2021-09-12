from celery import Celery
import os

app_celery = Celery(
    broker=f'pyamqp://admin:123mudar@{os.environ.get("HOST_RABBITMQ","localhost")}//'
)

def configure(app):
    app_celery.conf.update(app.config)


@app_celery.task()
def ola_mundo():
    return 'olá mundo'


def getMensagemRecurso():
    #buscar mensagem
    #criar recurso
    pass