import pika
import pg8000 as pgdb
import datetime
from time import sleep

sleep(10.0)

connection = pika.BlockingConnection(
  pika.URLParameters("amqp://queue:5672")
)
channel = connection.channel()
channel.queue_declare(queue='hello')

dbconn = pgdb.connect(
  host="database",
  user="exdb",
  password="exceptional71",
  database="exdb"
)
cursor = dbconn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS extable (
  id SERIAL PRIMARY KEY,
  message VARCHAR(255) NOT NULL
)
""")
dbconn.commit()

k = 0
def callback(ch, method, properties, body):
  data = body.decode()
  print(datetime.datetime.now(), data)
  cursor.execute("INSERT INTO extable (message) VALUES ('%s')" % (data))
  dbconn.commit()

  global k
  k += 1
  if k % 10 == 0:
    cursor.execute("SELECT COUNT(id) FROM extable")
    recs = cursor.fetchall()
    dbconn.commit()
    print(recs, "records in database")

channel.basic_consume(callback, queue='hello', no_ack=True)
channel.start_consuming()

