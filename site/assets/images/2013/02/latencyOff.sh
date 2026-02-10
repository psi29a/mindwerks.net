#!/bin/bash
# Remove all policies assigned to interfaces
/sbin/tc qdisc del dev p1p1 root
/sbin/tc qdisc del dev p1p2 root
/sbin/tc qdisc del dev p2p1 root
/sbin/tc qdisc del dev p2p2 root
/sbin/tc qdisc del dev p3p1 root
/sbin/tc qdisc del dev p3p2 root
