#!/bin/sh

cd /arcus/scripts/

#./arcus.sh deploy conf/local.sample.json
#./arcus.sh zookeeper init
./arcus.sh zookeeper start
./arcus.sh memcached register conf/local.sample.json
./arcus.sh memcached start test

./arcus.sh zookeeper stat
./arcus.sh memcached list test
while :
do
    sleep 10
    ./arcus.sh memcached list test
    date
done

