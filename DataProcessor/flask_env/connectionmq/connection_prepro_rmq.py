import pika

connection = None
channel = None


def initialize_rabbitmq():
    global connection, channel
    connection = pika.BlockingConnection(pika.ConnectionParameters('my_rabbitmq', heartbeat=600))
    channel = connection.channel()
    channel.queue_declare(queue='processing_queue')


def consume_rabbitmq():
    try:
        method_frame, header_frame, body = channel.basic_get(queue='processing_queue')
        return body
    except Exception as e:
        print(f"Error consuming RabbitMQ: {e}")
        return None
    finally:
        if connection and connection.is_open:
            connection.close()

