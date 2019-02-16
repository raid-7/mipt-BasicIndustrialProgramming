import pika
from time import sleep

sleep(10.0)

connection = pika.BlockingConnection(
  pika.URLParameters("amqp://queue:5672")
)
channel = connection.channel()
channel.queue_declare(queue='hello')
data = "a"
while True:
  channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=data.encode()
  )
  sleep(0.01)
