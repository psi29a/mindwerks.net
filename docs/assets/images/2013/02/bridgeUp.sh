#!/bin/bash

# Bring up the bridges
ifconfig p1p1 up
ifconfig p1p2 up
ifconfig p2p1 up
ifconfig p2p2 up
ifconfig p3p1 up
ifconfig p3p2 up

brctl addbr bridge1
brctl addif bridge1 p1p1
brctl addif bridge1 p1p2

brctl addbr bridge2
brctl addif bridge2 p2p1
brctl addif bridge2 p2p2

brctl addbr bridge3
brctl addif bridge3 p3p1
brctl addif bridge3 p3p2

ifconfig bridge1 up
ifconfig bridge2 up
ifconfig bridge3 up
