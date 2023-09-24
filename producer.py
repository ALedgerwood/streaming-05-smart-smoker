# producer.py
###Producer code for Module 5
#Alex Ledgerwood

# producer.py
import pandas as pd
import random
import time
import pika

# Load the CSV file
df = pd.read_csv('smoker-temps.csv')

# Initialize RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='temp_queue')

# Define a list of sensors
sensors = ['smoker', 'foodA', 'foodB']

# Simulate temperature readings and send them to RabbitMQ
for index, row in df.iterrows():
    Time = row['Time (UTC)']

    # Loop through the sensors and send data for each sensor
    for sensor in sensors:
        # Create a dictionary to represent the temperature readings
        temperature_reading = {
            'timestamp': Time,
            'sensor': sensor,
            'temperature': None  # Fill in the temperature value based on the sensor
        }

        if sensor == 'smoker':
            temperature_reading['temperature'] = row['Channel1'] + random.uniform(-1, 1)
        elif sensor == 'foodA':
            temperature_reading['temperature'] = row['Channel2'] + random.uniform(-1, 1)
        elif sensor == 'foodB':
            temperature_reading['temperature'] = row['Channel3'] + random.uniform(-1, 1)

        # Define message properties with the 'sensor' header
        properties = pika.BasicProperties(
            headers={'sensor': sensor}
        )

        # Send temperature readings to RabbitMQ with message properties
        channel.basic_publish(
            exchange='',
            routing_key='temp_queue',
            body=str(temperature_reading),
            properties=properties
        )

# Close the connection
connection.close()
