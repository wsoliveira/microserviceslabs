import pika
import os

def publish(fila, p_exchange, msg):
    credentials = pika.PlainCredentials('admin', '123mudar')
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ.get("HOST_RABBITMQ","127.0.0.1"), credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue=fila)
    channel.exchange_declare(exchange=p_exchange, exchange_type='direct')
    channel.queue_bind(fila, p_exchange, routing_key='')

    channel.basic_publish(exchange=p_exchange, routing_key='',
                      body=msg)
    connection.close()