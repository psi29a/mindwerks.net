---
date: 2012-06-18
categories:
  - Laptop
  - Operating Systems
  - Linux
  - Ubuntu
tags:
  - BCM4311
  - BCM4312
  - BCM4313
  - BCM4321
  - BCM4322
  - BCM43224
  - BCM43227
  - BCM43228
  - broadcom
  - kernel
  - linux
  - wireless
  - 3.4
  - 3.5
  - 3.6
  - Bret Curtis
---

# Wireless BCM4312 with the 3.4 and 3.5 kernel

![Broadcom Chipset BCM4312](../../assets/images/2011/03/BCM4312s.jpg){ align=left width="200" }

The hybrid driver from Broadcom is still a bit behind in terms of support for the latest kernels but there are workarounds. This particular issue also effects other kernel modules such as the out of tree Nvidia and ATI blobs that require the ***asm/system.h*** file in their includes.

I've had success with replacing it with ***asm/switch\_to.h*** which seems to have fixed things for now. The cause for this can be found on the [LKML](https://lkml.org/lkml/2012/3/29/360).

Chipsets supported by "Broadcom’s IEEE 802.11a/b/g/n hybrid Linux® device driver" are: BCM4311, BCM4312, BCM4313, BCM4321, BCM4322, BCM43224, and BCM43225, BCM43227 and BCM43228.

**Errors:**
> bcurtis@ronin:~/workspace/wl$ make
> KBUILD\_NOPEDANTIC=1 make -C /lib/modules/`uname -r`/build M=`pwd`
> make[1]: Entering directory `/usr/src/linux-headers-3.5.0-030500rc3-generic'
> Wireless Extension is the only possible API for this kernel version
> Using Wireless Extension API
> LD /home/bcurtis/workspace/wl/built-in.o
> CC /home/bcurtis/workspace/wl/src/shared/linux\_osl.o
> CC /home/bcurtis/workspace/wl/src/wl/sys/wl\_linux.o
> /home/bcurtis/workspace/wl/src/wl/sys/wl\_linux.c:43:24: fatal error: asm/system.h: No such file or directory
> compilation terminated.
> make[2]: \*\*\* Error 1
> make[1]: \*\*\* Error 2
> make[1]: Leaving directory `/usr/src/linux-headers-3.5.0-030500rc3-generic'
> make: \*\*\* Error 2

**The rundown:**

1. Download the 32 or 64-bit version:
   `http://www.broadcom.com/support/802.11/linux_sta.php`
2. Download my patches: [bc\_wl\_abiupdate.patch](../../assets/images/2011/11/bc_wl_abiupdate.patch) and [switch\_to.patch](../../assets/images/2012/06/switch_to.patch)
3. Extract the sources:
   `cd ~/Downloads; mkdir -p wl; cd wl; tar xf ../hybrid-portsrc*.tar.gz`
4. Patch and compile the sources:
   `patch -p0 src/wl/sys/wl_linux.c < ~/Downloads/switch_to.patch; patch -p0 src/wl/sys/wl_linux.c < ~/Downloads/bc_wl_abiupdate.patch;
   make; sudo make install; sudo depmod; sudo modprobe wl`

Give Ubuntu a few seconds after loading the "wl" kernel module, then eventually the Network Manager will start looking for wireless networks.

TL;DR: These patches are required for a working wl kernel module for the 3.4 and 3.5 kernel series.

**Update:** Also verified to work with Linux 3.6 series.
