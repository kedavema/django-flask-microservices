import pika
import json


params = pika.URLParameters(
    'amqps://zuzgwvtk:66ItdNU9bAI7mJskoOSkSZMrVnVdI_ci@snake.rmq2.cloudamqp.com/zuzgwvtk')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange='',
        routing_key='admin',
        body=json.dumps(body),
        properties=properties
    )
