import os
import json
import pika
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters(
    'amqps://zuzgwvtk:66ItdNU9bAI7mJskoOSkSZMrVnVdI_ci@snake.rmq2.cloudamqp.com/zuzgwvtk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    product_id = json.loads(body)
    product = Product.objects.get(id=product_id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(
    queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
