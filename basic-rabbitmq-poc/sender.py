#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
import json
import sys

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

    data = {}
    for param in sys.argv:
        data['data'] = param
        json_data = json.dumps(data)
        publishMessage(channel, json_data)

    connection.close()
    print('[x] -> Send body:', json_data)


def getRabbitConnection():
    credentials = pika.PlainCredentials(rabbit_username, rabbit_password)
    return pika.BlockingConnection(pika.ConnectionParameters(
        rabbit_host, rabbit_port, rabbit_virtual_host, credentials)
    )


def publishMessage(channel, message):
    channel.basic_publish(exchange='', routing_key='basic-events', body=message)


if __name__ == '__main__':
    run()
