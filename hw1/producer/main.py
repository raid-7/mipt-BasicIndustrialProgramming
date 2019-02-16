import pika
from time import sleep

connection = pika.BlockingConnection(
  pika.URLParameters("amqp://guest:guest@localhost:32769")
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
