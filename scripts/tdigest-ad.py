#!/usr/bin/python2.7
import kafka
from kafka import KafkaConsumer
import json
from tdigest import TDigest

consumer = KafkaConsumer('demo-topic', group_id=None, bootstrap_servers='127.0.0.1:9092', value_deserializer=lambda v: json.loads(v)) 

entity_detectors = {}
counter = 0 

for msg in consumer:
  entity_id = msg.value['id']
  value     = msg.value['value']

  if entity_id not in entity_detectors:
    entity_detectors[entity_id] = TDigest()
    
  #Get entity specific anomaly detector
  detector = entity_detectors[entity_id]

  #Check if detector is empty
  if( 10 > len(detector) ):
    detector.update(value)
    continue

  #Get bounds
  upp_bound = detector.percentile(99.9)
  low_bound = detector.percentile(0.1)

  #Display info
  if(0 == (counter%5)):
    print 'msg no. {}, entity {}, low {}, upp {}, {}'.format(counter, entity_id, low_bound, upp_bound, entity_detectors)

  counter += 1
  
  if( value < low_bound or value > upp_bound ):
    print '---> Entity {}, low {}, upp {}, anomalous value {}'.format(entity_id, low_bound, upp_bound, value) 
    detector.update(value, w=0.3)
  else:
    #Update detector (enables adapting to behaviour changes)
    detector.update(value)
