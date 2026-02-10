---
date: 2011-11-14
categories:
  - Code
  - C/C++
  - Laptop
  - Ubuntu
tags:
  - 3.2
  - BCM4311
  - BCM4312
  - BCM4313
  - BCM4321
  - BCM4322
  - BCM43224
  - BCM43227
  - BCM43228
  - wireless
  - broadcom
  - linux
  - kernel
  - Bret Curtis
---

# Wireless BCM4312 3.2 kernel

![Broadcom Chipset BCM4312](../../assets/images/2011/03/BCM4312s.jpg){ align=left width="200" }

Since there is an Ubuntu package 'firmware-b43-lpphy-installer' which is up to date and will work against the 3.0 kernel, my earlier posts are obsolete. If you are not running Ubuntu, then you will still need to reference my [post](https://mindwerks.net/2011/03/broadcom-ubuntu/).

The latest 3.2 Linux kernel however has a few ABI changes, most notably in the network stack which effects the Broadcom's wl module. Most notably is: ***.ndo\_set\_multicast\_list*** which was replaced with ***.ndo\_set\_rx\_mode***.

My specific chipset from lspci command:
> Broadcom Corporation BCM4312 802.11b/g LP-PHY (rev 01)

Below is the error I get with v5\_100\_82\_38 from Broadcom when compiling against Linux kernel 3.2:
> bcurtis@zwartevogel:~/Downloads/wl$ sudo make
> KBUILD\_NOPEDANTIC=1 make -C /lib/modules/3.2.0-030200rc1-generic/build M=`pwd`
> make[1]: Entering directory `/usr/src/linux-headers-3.2.0-030200rc1-generic'
> LD /home/bcurtis/Downloads/wl/built-in.o
> CC /home/bcurtis/Downloads/wl/src/shared/linux\_osl.o
> CC /home/bcurtis/Downloads/wl/src/wl/sys/wl\_linux.o
> /home/bcurtis/Downloads/wl/src/wl/sys/wl\_linux.c:326:2: error: unknown field ‘ndo\_set\_multicast\_list’ specified in initializer
> /home/bcurtis/Downloads/wl/src/wl/sys/wl\_linux.c:326:2: warning: initialization from incompatible pointer type
> /home/bcurtis/Downloads/wl/src/wl/sys/wl\_linux.c:326:2: warning: (near initialization for ‘wl\_netdev\_ops.ndo\_validate\_addr’)
> make[2]: \*\*\* Error 1
> make[1]: \*\*\* Error 2
> make[1]: Leaving directory `/usr/src/linux-headers-3.2.0-030200rc1-generic'
> make: \*\*\* Error 2

To get your wireless adapter working again:

1. Download this patch: [bc\_wl\_abiupdate.patch](../../assets/images/2011/11/bc_wl_abiupdate.patch)
2. `patch -p0 src/wl/sys/wl_linux.c < bc_wl_abiupdate.patch`
3. `sudo make; sudo make install; sudo depmod; sudo modprobe wl`

Give Ubuntu a few seconds after loading the "wl" kernel module, then eventually the Network Manager will start looking for wireless networks.

Chipsets supported by "Broadcom's IEEE 802.11a/b/g/n hybrid Linux® device driver" are: BCM4311, BCM4312, BCM4313, BCM4321, BCM4322, BCM43224, and BCM43225, BCM43227 and BCM43228.
