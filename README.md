# Prerequisites
Working docker environment.

# Run container
Script downloads and starts docker image ababolcai/hackaton-ad-image.
## For linux:
```sh
bash run-container-linux.sh
```
## For mac:
```bash
bash run-container-mac.sh
```

# Init environment
Creates kafka demo topic.
```bash
bash init-env.sh
```

# Demo scripts description
Short description of scripts used at hackaton
## Start generating sine wave data
Script starts to generate sine wave data in running container.
```bash
bash start-sine.sh
```

## Tail data stream
Script for consuming demo kafka topic
```bash
bash tail-stream.sh
```

## Start min-max "anomaly detector"
Starts simple min(-1) max(1) anomaly detector
```bash
bash start-min-max-ad.sh
```

## Start generating tooth wave data
Script starts to generate "tooth" wawe (..., 2, 2, 1, 1, 2, 2, 1, 1, ...).
```bash
bash start-tooth.sh
```

## Send anomalous data 
Script for sending data to demo kafka topic
```bash
bash send-anomalous-data.sh <id(int)> <value(int)>
```

## Start tdigest "anomaly detector"
Script starts anomaly detector based on Ted Dunnings [tdigest](https://github.com/tdunning/t-digest)
```bash
bash start-tdigest-ad.sh
```
