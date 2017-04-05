#!/bin/bash
echo "Demo env initialization"
/opt/kafka_2.11-0.10.1.0/bin/kafka-topics.sh --zookeeper localhost:2181 --create --topic demo-topic --partitions 1 --replication-factor 1
