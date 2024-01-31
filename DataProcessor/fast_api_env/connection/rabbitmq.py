import pika

connection = None
channel = None


def initialize_rabbitmq():
    global connection, channel
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('my_rabbitmq', heartbeat=600))
        channel = connection.channel()
        channel.queue_declare(queue='processing_queue')
    except pika.exceptions.AMQPConnectionError as e:
        print('Connection Error:', str(e))
    except pika.exceptions.AMQPChannelError as e:
        print('Channel Error Creation:', str(e))


def close_rabbitmq_connection():
    if connection is not None:
        connection.close()


def send_message(message):
    """
    Send the message to the queue through the channel.
    :param message:
    :return:
    """
    try:
        channel.basic_publish(exchange='',
                              routing_key='processing_queue',
                              body=message)
        return "Successfully 200."
    except Exception as e:
        return f"Error sending message: {str(e)}"
