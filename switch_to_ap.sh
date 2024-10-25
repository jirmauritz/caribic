#! /bin/bash

sudo systemctl stop dhcpcd
sudo systemctl start dhcpcd_ap
sudo systemctl start hostapd
sudo systemctl start dnsmasq
