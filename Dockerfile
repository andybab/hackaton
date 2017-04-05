FROM spotify/kafka:latest

RUN apt-get update && \
    apt-get install -y python-pip && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean && \
    pip install --upgrade pip && \
    pip install kafka

ADD scripts/demo-init-env.sh scripts/generate-sine.py scripts/generate-tooth.py /usr/local/bin/
