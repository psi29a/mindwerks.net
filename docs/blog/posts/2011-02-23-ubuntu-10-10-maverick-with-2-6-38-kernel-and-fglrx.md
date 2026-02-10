---
date: 2011-02-23
categories:
  - Video
  - Ubuntu
  - Software
tags:
  - 8.812
  - fglrx
  - ubuntu
  - linux
  - 2.6.38
  - kernel
  - Bret Curtis
---

# Ubuntu 10.10 Maverick with 2.6.38 kernel and fglrx 8.812

![glxgears](../../assets/images/2010/11/glxgears.png){ align=left width="200" }

[X-Swat](https://launchpad.net/~ubuntu-x-swat/+archive/x-updates)  has not updated their ati packages in a long time which means that Natty users and Maverick users with 2.6.38 (64-bit) cannot run with fglrx video drivers.

In order to get the latest 2.6.38 kernel and fglrx playing nicely together you will need to build these packages yourself.

**Custom build procedure:**

1. Install the latest 2.6.38 kernel revision from [Ubuntu Mainline](http://kernel.ubuntu.com/~kernel-ppa/mainline/).
2. Download [11.1](https://a248.e.akamai.net/f/674/9206/0/www2.ati.com/drivers/linux/ati-driver-installer-11-1-x86.x86_64.run) from [AMD](http://support.amd.com/us/gpudownload/linux/Pages/radeon_linux.aspx)
3. Extract the files from the package:
   `sh ./ati-driver-installer-11-1-x86.x86_64.run --extract ati`
4. Download the patch [here](../../assets/images/2011/02/2.6.38_console.patch), then apply it:
   `cd ati; patch -p1 < ../2.6.38_console.patch`
5. Build our new ati/fglrx deb packages:
   `./ati-installer.sh 8.812 --buildpkg Ubuntu/maverick`
6. Install our newly created deb packages:
   `sudo dpkg -i ../fglrx*.deb`
7. If your /etc/X11/xorg.conf is missing you will need to run:
   `sudo aticonfig --initial`
   and then reboot.

That newly created package should work for the entire 2.6.38 series.
