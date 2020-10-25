from kafka import KafkaConsumer
from json import loads, dumps
import queue
import requests
import pymongo
from kafka import KafkaProducer


# ROCKETS_STATES_BASE_URL = "http://localhost:2000/eventRegistration"


def getCurrentSatelliteName(rocketName):
    DELIVERY_STATES_BASE_URL = "http://localhost:7000"
    # Recuperation de la mission actuelle de la Rocket (PAST == FALSE)
    currentPayload = requests.get("{}/payload/payloadByRocketName/{}".format(DELIVERY_STATES_BASE_URL, rocketName))
    # print("\n-----------------\n")
    # print(currentPayload)
    # print("\n-----------------\n")
    return currentPayload.json()["satellite"]


EVENT_REGISTRATION_BASE_URL = "http://localhost:2000/eventRegistration"
queueresponse = queue.Queue()

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='logger-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(
    ['launcherTopic', 'pollelonresponsetopic', 'polltoryresponsetopic', 'Pollrequesttopic', 'rocketTopic'])

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


def logEventAndSendMessage(rocketName, siteName, message):
    x = requests.post(EVENT_REGISTRATION_BASE_URL, json={"rocketName": rocketName,
                                                         "siteName": siteName,
                                                         "satelliteName": getCurrentSatelliteName(rocketName),
                                                         "message": message})

    # SEND TO MARY DASHBOARD
    m = {'value': "ROCKET : " + rocketName + ", SATELLITE : " + getCurrentSatelliteName(
        rocketName) + ", LAUNCH SITE : " + siteName + " ||| " + message}
    producer.send('eventCollectortopic', value=m)


for msg in consumer:
    message = msg.value
    topic_retrieve = msg.topic

    if topic_retrieve == 'Pollrequesttopic':
        logEventAndSendMessage(message['rocketName'], message['siteName'], "Richard start Poll")
    elif topic_retrieve == 'pollelonresponsetopic':
        logEventAndSendMessage(message['request']['rocketName'], message['request']['siteName'],
                               "ELON response POLL : " + str(message['response']['status'] != "it's risky"))
    elif topic_retrieve == 'polltoryresponsetopic':
        logEventAndSendMessage(message['request']['rocketName'], message['request']['siteName'],
                               "TORY response POLL : " + str(message['response']['wind'] < 10))
    elif topic_retrieve == 'launcherTopic':
        logEventAndSendMessage(message['rocketName'], message['siteName'], message['action'])
    elif topic_retrieve == 'rocketTopic' and message['action'] == "running":
        logEventAndSendMessage(message['rocketName'], message['siteName'],
                               message['rocketName'] + " at position " + message['state'])