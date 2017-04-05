#!/bin/bash
docker exec -it demo-machine sh -c 'echo {\"id\": $0, \"value\": $1} | /opt/kafka_2.11-0.10.1.0/bin/kafka-console-producer.sh --broker-list=172.17.0.1:9092 --topic demo-topic' $1 $2
