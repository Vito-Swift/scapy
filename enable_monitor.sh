#!/bin/bash
ip link set edup-wlan0 down
iw edup-wlan0 set monitor control
ip link set edup-wlan0 up
iw dev edup-wlan0 set channel 36 80MHz
