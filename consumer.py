import json
import os

import pika

# django setup
# because we are using this file outside django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")

import django

django.setup()

from products.models import Product

rabbitMQ_url = 'amqps://gyjabiuq:T6BgZbtVk2_aoDzGG0tLXAu1CRRhMXea@lionfish.rmq.cloudamqp.com/gyjabiuq'

params = pika.URLParameters(url=rabbitMQ_url)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(channel_name, method, properties, body):
    print("Received in ADMIN - DJANGO APP")
    json_data = json.loads(body)
    print(json_data)
    product = Product.objects.get(id=json_data)

    product.likes = product.likes + 1
    product.save()

    print('Product likes increased...')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Started Consuming... [test-consumer in admin-django-microservice]")

channel.start_consuming()

# channel.close()
