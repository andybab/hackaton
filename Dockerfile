FROM spotify/kafka:latest

RUN apt-get update && \
    apt-get install -y python-numpy python-pip && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean && \
    pip install --upgrade pip && \
    pip install kafka tdigest

ADD scripts/demo-init-env.sh scripts/generate-sine.py scripts/generate-tooth.py scripts/min-max-ad.py /usr/local/bin/
