#!/usr/bin/env python
import pika
import json

rabbit_host = 'localhost'
rabbit_port = 5672
rabbit_virtual_host = '/'
rabbit_username = 'admin'
rabbit_password = 'admin'

def run():
    connection = getRabbitConnection()
    channel = connection.channel()
    # If queue already exists just don't do anything
    channel.queue_declare(queue='basic-events')

    print(' [*] Waiting for messages. To exit press CTRL+C')
    consumeMessages(channel)
    channel.start_consuming()


def getRabbitConnection():
    credentials = pika.PlainCredentials(rabbit_username, rabbit_password)
    return pika.BlockingConnection(pika.ConnectionParameters(
        rabbit_host, rabbit_port, rabbit_virtual_host, credentials)
    )


def consumeMessages(channel):
    channel.basic_consume(
        queue='basic-events', auto_ack=True, on_message_callback=callback
    )


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


if __name__ == '__main__':
    run()
