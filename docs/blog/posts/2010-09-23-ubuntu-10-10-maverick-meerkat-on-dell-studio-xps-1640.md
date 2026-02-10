---
date: 2010-09-23
categories:
  - Laptop
  - Ubuntu
  - Video
tags:
  - linux
  - ubuntu
  - meerkat
  - fglrx
  - radeon
  - dell studio
  - xps
  - xorg
  - xserver
  - Bret Curtis
---

# Ubuntu 10.10 Maverick Meerkat on Dell Studio XPS 1640

After a brief time with Karmic (10.04), the laptop was upgraded to the beta of Maverick. Everything works out of the box with no additional tricks necessary in getting the Dell Studio XPS 1640 fully functional.

![ubuntu-maverick-meerakat](../../assets/images/2010/09/ubuntu-maverick-meerakat.png){ align=left width="200" }

The only drawback I found in upgrading from Karmic was the loss of fglrx as a xorg-server driver. Maverick is shipping with the 1.9 version of xorg-server which is ABI incompatible with what fglrx is compiled against.

The exact error is:
`undefined symbol: savedScreenInfo`
which causes X not to start.

The [rumour](http://ubuntuforums.org/showthread.php?t=1549872) is that ATI will release a fglrx package that is compiled against 1.9 version of xorg-server when Maverick ships on Sunday, October 10th.

Compiling the fglrx against the latest kernel is also not a problem if you follow the advice found [here](http://aur.archlinux.org/packages.php?ID=29111).

This does not impact a good desktop experience with your "Visual Effects" set to "Normal". By default, Maverick ships with the latest radeon driver that xorg-server which is good enough to handle all those lovely desktop effects. I recommend this driver over fglrx because:

- it is opensource
- has acceptable 2d/3d performance
- it is not a resource hog
- the laptop will no longer burn your lap

I will continue testing against fglrx and I look forward to the final release.

[Maverick Meerkat Release Schedule](https://wiki.ubuntu.com/MaverickReleaseSchedule)

UPDATE: If you have upgraded to Maverick and switched to the radeon driver after first having fglrx, you will need to purge your fglrx drivers. What happens is that X will start with the radeon driver but load your fglrx glx libraries and cause a segmentation fault or garbled screen.

To fix this:
`aptitude purge fglrx fglrx-amdcccle fglrx-modaliases xorg-driver-fglrx fglrx-dev`
