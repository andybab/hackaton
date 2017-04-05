#!/bin/bash

#Remove container if exists
docker container rm demo-machine

#Run container
docker run -h demo-machine  --name demo-machine -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=`/sbin/ifconfig docker0 | grep 'inet ' | cut -d: -f2 | awk '{ print $2}'` --env ADVERTISED_PORT=9092 ababolcai/hackaton-ad-image 
