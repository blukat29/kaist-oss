#!/bin/sh

VBoxManage modifyvm "default" --natpf1 "arcus_zk,tcp,,2181,,2181";
VBoxManage modifyvm "default" --natpf1 "arcus_mc1,tcp,,11211,,11211";
VBoxManage modifyvm "default" --natpf1 "arcus_mc2,tcp,,11212,,11212";

VBoxManage modifyvm "default" --natpf1 "hubble_web,tcp,,8000,,8000";
VBoxManage modifyvm "default" --natpf1 "hubble_server,tcp,,30000,,30000";
VBoxManage modifyvm "default" --natpf1 "hubble_listener,tcp,,30001,,30001";
