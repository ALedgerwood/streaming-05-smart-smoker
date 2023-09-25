### Alex Ledgerwood 9/24/2023
# streaming-05-smart-smoker

#I used chat gpt to develop the overall structure of the code, comparing its suggestions to the exisitng code of previous projects. I'm pretty pleased with the similarities I was able to keep to existing code blocks #from other modules, as specified in the assignment. Even using AI suggestions for code and existing coure code, I had to do a lot of debugging and ask a lot of follow up questions to keep modifying the code to fit #the assignment objectives, including adding filers in the callbacks to return data from just one column of the csv file per consumer.

#I got all three consumers receiving message from the producer, but they were getting the whole csv data. So to ensure that each consumer only receives a subset of the data, I had to implement a message filtering #mechanism. I did this by using message headers or properties to tag the messages and having consumers filter based on those tags. I made these changes to the callback.

###Info on the project from the course site

# We want to stream information from a smart smoker. Read one value every half minute. (sleep_secs = 30)

#smoker-temps.csv has 4 columns:

#[0] Time = Date-time stamp for the sensor reading
#[1] Channel1 = Smoker Temp --> send to message queue "01-smoker"
#[2] Channel2 = Food A Temp --> send to message queue "02-food-A"
#[3] Channel3 = Food B Temp --> send to message queue "03-food-B"


#Sensors
#We have temperature sensors track temperatures and record them to generate a history 

#Streaming Data
#Our thermometer records three temperatures every thirty seconds (two readings every minute). The three #temperatures are:

#the temperature of the smoker itself.
#the temperature of the first of two foods, Food A.
#the temperature for the second of two foods, Food B.
 

#Significant Events - OPTIONAL
#We want know if:
#The smoker temperature decreases by more than 15 degrees F in 2.5 minutes (smoker alert!)
#Any food temperature changes less than 1 degree F in 10 minutes (food stall!)
 

#Smart System
#We will use Python to:

#Simulate a streaming series of temperature readings from our smart smoker and two foods.
#Create a producer to send these temperature readings to RabbitMQ.
#Create three consumer processes, each one monitoring one of the temperature streams. 
#Perform calculations to determine if a significant event has occurred. OPTIONAL
