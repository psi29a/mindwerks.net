---
date: 2011-04-28
categories:
  - Video
  - Ubuntu
  - Software
tags:
  - 11.04
  - natty
  - fglrx
  - 2.6.39
  - ubuntu
  - linux
  - Bret Curtis
---

# Ubuntu 11.04 Natty with fglrx and 2.6.39

![glxgears](../../assets/images/2010/11/glxgears.png){ align=left width="200" }

Natty (11.04) users can finally get fglrx playing nicely together with X.org 1.10. We can also make the latest driver work well with the 2.6.39 kernel.

**Custom build procedure:**

1. Install the latest 2.6.39 kernel revision from [Ubuntu Mainline](http://kernel.ubuntu.com/~kernel-ppa/mainline/) or install the [PPA](https://launchpad.net/~kernel-ppa/+archive/ppa).
2. Download 64-bit [11.4](http://www2.ati.com/drivers/linux/ati-driver-installer-11-4-x86.x86_64.run).
3. Extract the files from the package:
   `sh ./ati-driver-installer-11-4-x86.x86_64.run --extract ati`
4. For 2.6.39 support, download this extra patch: [2.6.39\_bkl.patch](../../assets/images/2011/03/2.6.39_bkl.patch)
5. Check for Big Kernel Lock usage:
   `` cat /lib/modules/`uname -r`/build/.config | grep -c CONFIG_BKL=y ``
   If the result of this command is 0, then download [no\_bkl.patch](../../assets/images/2011/03/no_bkl.patch) as well.
6. then apply them:
   `cd ati; for i in ../*.patch; do patch -p1 < $i; done`
7. Build your new ati/fglrx deb packages:
   `./ati-installer.sh 8.841 --buildpkg Ubuntu/natty`
8. Install our newly created deb packages:
   `sudo dpkg -i ../fglrx*.deb`
9. If your /etc/X11/xorg.conf is missing you will need to run:
   `sudo aticonfig --initial`
   and then reboot.

That newly created package should work for the entire 2.6.39 series.
