---
date: 2011-06-01
categories:
  - C/C++
  - Laptop
  - Linux
tags:
  - BCM4311
  - BCM4312
  - BCM4313
  - BCM4321
  - BCM4322
  - BCM43224
  - BCM43227
  - BCM43228
  - linux
  - 3.0
  - kernel
  - wireless
  - BCM43225
  - Bret Curtis
---

# Wireless BCM4312 3.0 kernel

![Broadcom Chipset BCM4312](../../assets/images/2011/03/BCM4312s.jpg){ align=left width="200" }

With the latest 3.0 kernel there is still no "out of the box" support for my BCM4312 wireless chipset. Nor is there any help from Ubuntu 11.04 leaving me to use Broadcoms hybrid driver with patch.

Chipsets supported by "Broadcom's IEEE 802.11a/b/g/n hybrid Linux® device driver" are: BCM4311, BCM4312, BCM4313, BCM4321, BCM4322, BCM43224, and BCM43225, BCM43227 and BCM43228.

My specific chipset from lspci command:
> Broadcom Corporation BCM4312 802.11b/g LP-PHY (rev 01)

Below is the error I get with v5\_100\_82\_38 from Broadcom when compiling against Linux kernel 3.0:
> bcurtis@zwartevogel:~/Downloads/wl.org$ make
> KBUILD\_NOPEDANTIC=1 make -C /lib/modules/`uname -r`/build M=`pwd`
> make[1]: Entering directory `/usr/src/linux-headers-2.6.38-020638-generic'
> LD /home/bcurtis/Downloads/wl.org/built-in.o
> CC /home/bcurtis/Downloads/wl.org/src/shared/linux\_osl.o
> CC /home/bcurtis/Downloads/wl.org/src/wl/sys/wl\_linux.o
> /home/bcurtis/Downloads/wl.org/src/wl/sys/wl\_linux.c: In function ‘wl\_attach’:
> /home/bcurtis/Downloads/wl.org/src/wl/sys/wl\_linux.c:485:3: error: implicit declaration of function ‘init\_MUTEX’
> make[2]: \*\*\* Error 1
> make[1]: \*\*\* Error 2
> make[1]: Leaving directory `/usr/src/linux-headers-3.0.0-0300rc1-generic'
> make: \*\*\* Error 2

To get your wireless adapter working again:

1. Download the 32 or 64-bit version:
   `http://www.broadcom.com/support/802.11/linux_sta.php`
2. Download my patch for > 2.6.37 support:
   [broadcom-sta\_4\_kernel-2.6.38.patch](../../assets/images/2011/03/broadcom-sta_4_kernel-2.6.38.patch)
3. Extract the sources:
   `cd ~/Downloads; mkdir -p wl; cd wl; tar xf ../hybrid-portsrc*-v5_100_82_38.tar.gz`
4. Patch the sources, compile and install:
   `patch -p1 < ../broadcom-sta_4_kernel-2.6.38.patch
   make; sudo make install; sudo depmod; sudo modprobe wl`

Give Ubuntu a few seconds after loading the "wl" kernel module, then eventually the Network Manager will start looking for wireless networks.
