from xmlrpc.server import SimpleXMLRPCServer
import requests
import json
import time
import socket
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
from kafka import KafkaConsumer
from kafka import KafkaProducer

# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 9292  # Port to listen on (non-privileged ports are > 1023)
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
BASE_URL = "http://localhost:7000/payload"
ROCKET_DESTRUCTION = "destroy"
STAGE_SEPARATION = "Stage separation"
PAYLOAD_TOPIC = "payloadTopic"
PAYLOAD_SEPARATION = "Payload separation"
RUNNING = "running"
destroy = False
isStarted = False
rocketN = ""
siteN = ""
# payload = SimpleXMLRPCServer(('localhost', 8282), logRequests=True, allow_none=True)

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')

time.sleep(20)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='payload-simulation-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))


consumer.subscribe(['launcherTopic'])


def getCurrentSatelliteName(rocketName):
    DELIVERY_STATES_BASE_URL = "http://localhost:7000"
    # Recuperation de la mission actuelle de la Rocket (PAST == FALSE)
    currentPayload = requests.get("{}/payload/payloadByRocketName/{}".format(DELIVERY_STATES_BASE_URL, rocketName))
    print("\n-----------------\n")
    # print(currentPayload)
    print("\n-----------------\n")
    return currentPayload.json()["satellite"]


for msg in consumer:
    message = msg.value
    #
    # if destroy and not isStarted:
    #     print("destruction possible")
    #     data = {'action': ROCKET_DESTRUCTION,
    #             'siteName': siteN,
    #             'rocketName': rocketN
    #             # 'payloadName': getCurrentSatelliteName(rocketName),
    #             }
    #     producer.send(PAYLOAD_TOPIC, value=data)
    #     destroy = False

    if msg.topic == 'launcherTopic' and message['action'] == PAYLOAD_SEPARATION:
        print(message['action'])
        isStarted = True
        siteName = message['siteName']
        rocketName = message['rocketName']
        someRocketStates = json.loads(
            dumps(db.rocketsStates.find_one({"rocketName": rocketName, "siteName": siteName})))
        paylaodStatesArray = someRocketStates["payloadStatesHe"]
        print("SecondState started: payload telemetry")
        l = len(paylaodStatesArray)
        for index in range(0, l):
            responseDestruction = requests.get(
                "{}/rocketsStates/destructionA/{}/{}".format("http://localhost:5000", siteName, rocketName))
            if responseDestruction.text == "True":
                print("--------------- ANOMALY DESTRUCTION ACTIVATED")
                break
            time.sleep(5)

            data = {'action': RUNNING,
                    'siteName': siteName,
                    'payloadName': getCurrentSatelliteName(rocketName),
                    'rocketName': rocketName,
                    'state': str(paylaodStatesArray[index])}
            producer.send(PAYLOAD_TOPIC, value=data)

            if index == l - 1:
                data = {'action': "end",
                        'siteName': siteName,
                        'payloadName': getCurrentSatelliteName(rocketName),
                        'rocketName': rocketName,
                        'state': str(paylaodStatesArray[index])}
                producer.send(PAYLOAD_TOPIC, value=data)

        isStarted = False
