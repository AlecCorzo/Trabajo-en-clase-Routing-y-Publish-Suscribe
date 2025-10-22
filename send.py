import pika
import time
import os

time.sleep(10)

rabbit_host = os.getenv("RABBITMQ_HOST", "rabbitmq")
rabbit_port = int(os.getenv("RABBITMQ_PORT", 5672))
rabbit_user = os.getenv("RABBITMQ_USER", "guest")
rabbit_pass = os.getenv("RABBITMQ_PASS", "guest")

credentials = pika.PlainCredentials(rabbit_user, rabbit_pass)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, port=rabbit_port, credentials=credentials)
)

channel = connection.channel()
channel.queue_declare(queue="hola")

channel.basic_publish(exchange="", routing_key="hola", body="Hola desde Python y RabbitMQ")
print("Mensaje enviado")

connection.close()
