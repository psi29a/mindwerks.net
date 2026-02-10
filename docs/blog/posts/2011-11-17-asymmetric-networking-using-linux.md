---
date: 2011-11-17
categories:
  - Networking
  - Servers
  - Linux
  - Ubuntu
tags:
  - linux
  - kernel
  - networking
  - martians
  - Reverse Path Filtering
  - packetss
  - filter_rp
  - NIC
  - Bret Curtis
---

# Asymmetric networking using Linux

![asymmetric_network_icon](../../assets/images/2011/11/asymmetric_network_icon.jpg){ align=left width="128" }

The idea is simple, two subnets (separate networks) and then route packets from one to the other. The environment, however, is not symmetric. We wanted to contact a node on the other subnet and we could see the packets travelling over the switch to the router back through another switch to the node, but the node itself refused to reply.
Each node has two NICs and each NIC is connected to a separate network. If you try to connect or ping one node from another, Linux is smart enough to go directly over the NIC with the right network. If a NIC should ever fail, the failover is that the packets are then routed up one network to the router then over to the other network.
The network looks something like this:

```
        ----(router)----
        |               |
        |               |
   | switch |__  __| switch |
        |      \/       |
        |      /\       |
        |     /  \      |
        |    x    \     |
   | node1 |/      \| node2 |

note: The x is the broken link.
```

Apparently when going from node1 to node2 is not the problem, node2 just does not respond. This has to do [Reverse Path Filtering](http://www.linuxdocs.org/HOWTOs/Adv-Routing-HOWTO-12.html "Advanced Routing") and per default is enabled in the Linux kernel.
From the manual:
> By default, routers route everything, even packets which 'obviously' don't belong on your network. A common example is private IP space escaping onto the internet. If you have an interface with a route of 195.96.96.0/24 to it, you do not expect packets from 212.64.94.1 to arrive there.
> ...
> Basically, if the reply to this packet wouldn't go out the interface this packet came in, then this is a bogus packet and should be ignored.

Armed with this new knowledge and acknowledging that this system will not be on an Internet route-able environment, we decided to turn off the filtering.
`for i in /proc/sys/net/ipv4/conf/*/rp_filter ; do echo 0 > $i; done`
This solved the problem and node2 could reply back over it's NIC to the other network without having to go back through the router.
