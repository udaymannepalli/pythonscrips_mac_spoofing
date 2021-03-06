#! /usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's Mac address")

parser.parse_args()

interface = input("interface > ")
new_mac = input("new_mac > ")

print("[+] Changing the MAC address for" + interface + " to " + new_mac)

subprocess.call("ifconfig", interface, "down")
subprocess.call("ifconfig", interface, "hw", "ether", new_mac)
subprocess.call("ifconfig", interface, "up")