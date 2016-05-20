#!/bin/sh
docker run --rm \
    --name arcus1 \
    -p 2181:2181 -p 11211:11211 -p 11212:11212 \
    -it arcus
