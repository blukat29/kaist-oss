#!/bin/sh
mkdir -p log
docker run \
    --rm \
    -v $(pwd)/log:/log \
    -p 30000:30000 \
    -p 30001:30001 \
    -p 8000:8000 \
    --link arcus1:arcus \
    -it hubble
