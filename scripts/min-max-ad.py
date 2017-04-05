#!/usr/bin/python2.7
import kafka
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('demo-topic', bootstrap_servers='127.0.0.1:9092', value_deserializer=lambda v: json.loads(v)) 

for msg in consumer:
  entity_id = msg.value['id']
  value     = msg.value['value']

  if( value < -1 or value > 1 ):
    print 'Entity {}, anomalous value {}'.format(entity_id, value) 
