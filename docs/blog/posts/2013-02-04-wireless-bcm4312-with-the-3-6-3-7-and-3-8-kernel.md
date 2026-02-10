---
date: 2013-02-04
categories:
  - Laptop
  - Operating Systems
  - Linux
  - Ubuntu
tags:
  - 3.6
  - 3.7
  - 3.8
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
  - Bret Curtis
---

# Wireless BCM4312 with the 3.6, 3.7 and 3.8 kernel

![Broadcom Chipset BCM4312](../../assets/images/2011/03/BCM4312s.jpg){ align=left width="200" }

 As a follow up to , I've also tested the Broadcom hybrid driver with the 3.6, 3.7 and the soon to be released 3.8 kernels with success. There have been no major changes that should effect the operation of this driver.

To verify that everything is working as expected on the software side, when modprobe or insmod wl, you should get a similar dmesg output:

> [ 307.560347] lib80211: common routines for IEEE802.11 drivers
> [ 307.560353] lib80211\_crypt: registered algorithm 'NULL'
> [ 307.564524] wl: module license 'unspecified' taints kernel.
> [ 307.564529] Disabling lock debugging due to kernel taint

The only real issue at this point is this:
> WARNING: modpost: missing MODULE\_LICENSE() in /home/bcurtis/workspace/wl/wl.o
> see include/linux/module.h for more information
> WARNING: modpost: Found 1 section mismatch(es).
> To see full details build your kernel with:
> 'make CONFIG\_DEBUG\_SECTION\_MISMATCH=y'
> CC /home/bcurtis/workspace/wl/wl.mod.o
> LD /home/bcurtis/workspace/wl/wl.ko

While these aren't errors, they are problems to be addressed upstream by Broadcom if they wish to see their driver to be used in the future. They will also need to incorporate my patch sets from my previous post. They haven't updated their driver in about two years now.
