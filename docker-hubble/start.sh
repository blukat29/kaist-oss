#!/bin/sh

mkdir -p /log
cd hubblemon
python3 collect_server/run_server.py > /log/server.log 2> /log/server.err &
python3 collect_server/run_listener.py > /log/listener.log 2> /log/listener.err &
python3 collect_client/run_client.py > /log/client.log 2> /log/client.err &
python3 manage.py runserver 0.0.0.0:8000
