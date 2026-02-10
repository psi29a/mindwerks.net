---
date: 2013-10-03
categories:
  - Laptop
  - Linux
  - Ubuntu
tags:
  - 3.10
  - 3.11
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
  - ubuntu
  - 13.10
  - saucy
  - wireless
  - 3.12
  - Bret Curtis
---

# Wireless BCM4312 with the 3.10, 3.11, 3.12 and 3.13 kernels

![Broadcom Chipset BCM4312](../../assets/images/2011/03/BCM4312s.jpg){ align=left width="200" }

The hybrid driver from Broadcom was updated again in September (2013) with all the previous patches and a few other fixes as well. This brings them up to support linux kernel 3.9, which is very much welcome.

Sadly it breaks again with >= 3.10 with many warnings and errors which isn't good considering that Ubuntu (13.10) Saucy Salamander is about to be released.

We do have a patch for you though that gets us working again up to the 3.11 kernel.

Chipsets supported by "Broadcom’s IEEE 802.11a/b/g/n hybrid Linux® device driver" are: BCM4311, BCM4312, BCM4313, BCM4321, BCM4322, BCM43224, BCM43225, BCM43227 and BCM43228.

**The error you will run into:**
> bcurtis@Aria:~/Workspace/wl.orig$ make
> KBUILD\_NOPEDANTIC=1 make -C /lib/modules/`uname -r`/build M=`pwd`
> make[1]: Entering directory `/usr/src/linux-headers-3.11.0-11-generic'
> CFG80211 API is prefered for this kernel version
> Using CFG80211 API
> LD /home/bcurtis/Workspace/wl.orig/built-in.o
> CC /home/bcurtis/Workspace/wl.orig/src/shared/linux\_osl.o
> CC /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.o
> /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.c: In function ‘wl\_tkip\_printstats’:
> /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.c:3246:7: warning: passing argument 1 of ‘wl->tkipmodops->print\_stats’ from incompatible pointer type
> wl->tkip\_bcast\_data);
> ^
> /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.c:3246:7: note: expected ‘struct seq\_file \*’ but argument is of type ‘char \*’
> /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.c:3249:4: warning: passing argument 1 of ‘wl->tkipmodops->print\_stats’ from incompatible pointer type
> wl->tkipmodops->print\_stats(debug\_buf, wl->tkip\_ucast\_data);
> ^
> /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.c:3249:4: note: expected ‘struct seq\_file \*’ but argument is of type ‘char \*’
> /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.c: In function ‘wl\_reg\_proc\_entry’:
> /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.c:3470:2: error: implicit declaration of function ‘create\_proc\_entry’ [-Werror=implicit-function-declaration]
> if ((wl->proc\_entry = create\_proc\_entry(tmp, 0644, NULL)) == NULL) {
> ^
> /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.c:3470:22: warning: assignment makes pointer from integer without a cast
> if ((wl->proc\_entry = create\_proc\_entry(tmp, 0644, NULL)) == NULL) {
> ^
> /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.c:3475:16: error: dereferencing pointer to incomplete type
> wl->proc\_entry->read\_proc = wl\_proc\_read;
> ^
> /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.c:3476:16: error: dereferencing pointer to incomplete type
> wl->proc\_entry->write\_proc = wl\_proc\_write;
> ^
> /home/bcurtis/Workspace/wl.orig/src/wl/sys/wl\_linux.c:3477:16: error: dereferencing pointer to incomplete type
> wl->proc\_entry->data = wl;
> ^
> cc1: some warnings being treated as errors
> make[2]: \*\*\* Error 1
> make[1]: \*\*\* Error 2
> make[1]: Leaving directory `/usr/src/linux-headers-3.11.0-11-generic'
> make: \*\*\* Error 2

**The rundown:**

1. Download the 32 or 64-bit version:
   `http://www.broadcom.com/support/802.11/linux_sta.php`
2. Download the patch: [wl\_3.10.patch](../../assets/images/2013/10/wl_3.10.patch)
3. Extract the sources:
   `cd ~/Downloads; mkdir -p wl; cd wl; tar xf ../hybrid-*.tar.gz`
4. Patch and compile the sources: `patch -p2 < ~/Downloads/wl_3.10.patch; make; sudo make install; sudo depmod; sudo modprobe wl`

Give Ubuntu a few seconds after loading the "wl" kernel module, then eventually the Network Manager will start looking for wireless networks.

TL;DR: These patches are required for a working wl kernel module for the 3.10 and 3.11 kernel series.

**Update (2014-04-22):** Known to also work with Raring (14.04) that uses the 3.13 kernel.
