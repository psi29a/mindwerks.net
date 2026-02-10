#!/bin/bash

# Bring down the bridges
ifconfig bridge1 down
ifconfig bridge2 down
ifconfig bridge3 down

brctl delif bridge1 p1p1
brctl delif bridge1 p1p2
brctl delbr bridge1

brctl delif bridge2 p2p1
brctl delif bridge2 p2p2
brctl delbr bridge2

brctl delif bridge3 p3p1
brctl delif bridge3 p3p2
brctl delbr bridge3

ifconfig p1p1 down
ifconfig p1p2 down
ifconfig p2p1 down
ifconfig p2p2 down
ifconfig p3p1 down
ifconfig p3p2 down
