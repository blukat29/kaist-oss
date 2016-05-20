# docker-hubble

Hubblemon image that monitors local Arcus cloud.

An acrus cloud inside a docker container named `arcus1` must be running
and its zookeeper port must be 2181.

```
docker build -t hubble .
./run.sh
```

Then connect to `localhost:8000`

