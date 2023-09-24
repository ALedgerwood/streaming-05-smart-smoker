#consumer foodB
#Alex Ledgerwood
# consumer_foodB.py
import pika

# Consumer function for smoker temperature
def consume_foodB_temperature():
    # Initialize RabbitMQ connection and channel (similar to the producer)
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the same queue as the producer
    channel.queue_declare(queue='temp_queue')

    def callback(ch, method, properties, body):
        if 'sensor' in properties.headers and properties.headers['sensor'] == 'foodB':
            print("Received:", body) 

    # Set up a consumer to receive messages
    channel.basic_consume(queue='temp_queue', on_message_callback=callback, auto_ack=True)

    # Start consuming
    print("Consumer for foodB temperature is waiting for messages...")
    channel.start_consuming()

if __name__ == '__main__':
    consume_foodB_temperature()
