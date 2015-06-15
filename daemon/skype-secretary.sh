#!/bin/sh
export DISPLAY=:10
cd /opt/skype-secretary/daemon
while true;
    do
    ./skype_daemon.py
    done