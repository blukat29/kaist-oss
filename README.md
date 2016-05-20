### Port forwarding script

Turn off any running docker containers. Then turn off boot2docker machine.

```
docker machine stop default
```

Then add port forwarding settings

```
sh portforward.sh
```

Finally, restart boot2docker machine.

```
docker-machine start default
```
