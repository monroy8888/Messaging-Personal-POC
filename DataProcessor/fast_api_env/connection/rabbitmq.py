import pika
import pdb
import json

connection = None
channel = None


def initialize_rabbitmq():
    global connection, channel
    try:
        if connection is None or connection.close:
            connection = pika.BlockingConnection(pika.ConnectionParameters('my_rabbitmq', heartbeat=600))
        if channel is None or channel.is_closed:
            channel = connection.channel()
            channel.queue_declare(queue='processing_queue')
    except pika.exceptions.AMQPConnectionError as e:
        print('Connection Error:', str(e))
    except pika.exceptions.AMQPChannelError as e:
        print('Channel Error Creation:', str(e))


def close_rabbitmq_connection():
    if connection is not None and connection.is_open:
        connection.close()


def check_rabbitmq_status():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('my_rabbitmq'))
        channel = connection.channel()
        print("Connected to RabbitMQ successfully.")
        print(f"Is open: {connection.is_open}")
        print(f"Is closed: {connection.is_closed}")
        print(f"Channel is open: {channel.is_open}")
        print(f"Channel is closed: {channel.is_closed}")
    except pika.exceptions.AMQPConnectionError as e:
        print('Connection Error:', str(e))
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


def send_message(message):
    try:
        status_rabbitMQ = check_rabbitmq_status()

        if channel is None or channel.is_closed:
            initialize_rabbitmq()

        # Convierte el objeto a una cadena JSON antes de enviarlo
        serialized_message = json.dumps(message.json())

        channel.basic_publish(exchange='',
                              routing_key='processing_queue',
                              body=serialized_message)
        return "Successfully 200."
    except pika.exceptions.AMQPError as e:
        return f"""Error sending message -> -> : {str(e)}
            Rabbit status {str(status_rabbitMQ)}
        """

