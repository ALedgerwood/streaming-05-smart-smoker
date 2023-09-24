#Smart Smoker - Module 5
#Alex Ledgerwood

import pandas as pd
import random
import time

# Loading the CSV file 
df = pd.read_csv('smoker-temps.csv')


#[0] Time = Date-time stamp for the sensor reading
#[1] Channel1 = Smoker Temp --> send to message queue "01-smoker"
#[2] Channel2 = Food A Temp --> send to message queue "02-food-A"
#[3] Channel3 = Food B Temp --> send to message queue "03-food-B"

# Get temperature readings and send them to RabbitMQ
for index, row in df.iterrows():
    Channel1 = row['Channel1'] + random.uniform(-1, 1)  # Simulate smoker temperature
    Channel2 = row['Channel2'] + random.uniform(-1, 1)  # Simulate food A temperature
    Channel3 = row['Channel3'] + random.uniform(-1, 1)  # Simulate food B temperature
    Time = row['Time (UTC)']

    # Create a dictionary to represent the temperature readings
    temperature_reading = {
        'timestamp': Time,
        '01-smoker': Channel1,
        '02-food-A': Channel2,
        '03-food-B': Channel3
    }
# Send the temperature readings to RabbitMQ producer
import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue 
channel.queue_declare(queue='temp_queue')

# Send temperature readings to RabbitMQ
def send_temperature(temperature_reading):
    channel.basic_publish(
        exchange='',
        routing_key='temp_queue',
        body=str(temperature_reading)
    )

# Close the connection when done
connection.close()

import multiprocessing

# Consumer function for smoker temperature
def consume_smoker_temperature():
    # Initialize RabbitMQ connection and channel (similar to the producer)
    # Consume messages from the 'temperature_queue' and process them
    pass

# Consumer function for food 1 temperature
def consume_foodA_temperature():
    # Initialize RabbitMQ connection and channel (similar to the producer)
    # Consume messages from the 'temperature_queue' and process them
    pass

# Consumer function for food 2 temperature
def consume_foodB_temperature():
    # Initialize RabbitMQ connection and channel (similar to the producer)
    # Consume messages from the 'temperature_queue' and process them
    pass

if __name__ == '__main__':
    # Create three consumer processes
    smoker_process = multiprocessing.Process(target=consume_smoker_temperature)
    foodA_process = multiprocessing.Process(target=consume_foodA_temperature)
    foodB_process = multiprocessing.Process(target=consume_foodB_temperature)

    # Start the consumer processes
    smoker_process.start()
    foodA_process.start()
    foodB_process.start()

    # Wait for the processes to finish 
    smoker_process.join()
    foodA_process.join()
    foodB_process.join()

    # Sleep for a while to simulate streaming behavior
    time.sleep(30) 
