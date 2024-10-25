#! /bin/bash

sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
sudo systemctl stop dhcpcd_ap
sudo systemctl start dhcpcd
