#!/bin/bash
# Apply delay policies on interfaces
tc qdisc replace dev p1p1 root netem delay 16ms
tc qdisc replace dev p1p2 root netem delay 16ms
tc qdisc replace dev p2p1 root netem delay 20ms
tc qdisc replace dev p2p2 root netem delay 20ms
tc qdisc replace dev p3p1 root netem delay 173ms
tc qdisc replace dev p3p2 root netem delay 173ms
