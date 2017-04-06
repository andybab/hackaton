#!/usr/bin/python2.7
import kafka
from kafka import KafkaProducer
import json
from math import sin
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8')) 

while True:
  producer.send('demo-topic', {'id': 0, 'value': sin(time.time() / 3)})
  time.sleep(0.2)
