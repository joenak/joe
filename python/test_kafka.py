import json

from kafka import KafkaConsumer

kafka_topic = 'joe'
kafka_brokers = '172.16.248.30:9092'

consumer = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_brokers, auto_offset_reset='earliest')

for message in consumer:
    jdata = json.loads(message.value)
    print(jdata)
