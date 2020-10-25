from bson.json_util import dumps, loads
from xmlrpc.client import ServerProxy
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='gwine-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(['payloadTopic'])

for msg in consumer:
    message = msg.value
    if (message['action'] == "running"):
        print("Données telemetriques ==========> ", end='')
        print(message['payloadName'] + " at position " + message['state'])