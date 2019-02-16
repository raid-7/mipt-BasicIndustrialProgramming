import pika
from time import sleep
import random

sleep(10.0)

connection = pika.BlockingConnection(
  pika.URLParameters("amqp://queue:5672")
)
channel = connection.channel()
channel.queue_declare(queue='hello')

while True:
  data = "rnd" + str(random.randrange(0, 2**24))
  channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=data.encode()
  )
  sleep(0.01)
