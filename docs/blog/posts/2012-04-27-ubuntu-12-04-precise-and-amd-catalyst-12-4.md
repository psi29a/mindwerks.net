---
date: 2012-04-27
categories:
  - Laptop
  - Video
  - Ubuntu
tags:
  - 3.2
  - kernel
  - fglrx
  - amd
  - precise
  - ubuntu
  - 12.04
  - LTS
  - Bret Curtis
---

# Ubuntu 12.04 (Precise) and AMD Catalyst 12.4

![glxgears](../../assets/images/2010/11/glxgears.png){ align=left width="200" }

Precise Pangola has been released and a day later comes a new fglrx driver. While there isn't a changelog, this build apparently gives us:
> early-look support for Ubuntu 12.04, Linux PowerXpress support for the Intel Ivy Bridge platform, packaging script updates, and various bug-fixes.

Among the bug-fixes for Catalyst 12.4 on Linux are: fixing some multi-head issues, a system hang in certain PowerXpress configurations, fixing a system hang when using OpenGL overlays, correcting an OpenGL performance drop, a soft-hang when killing the X Server, and severe corruption for OpenGL games using the AMD "Redwood" graphics processors.

**If you want to build these for yourself then you can follow these instructions:**

1. Download 64-bit [12.4](http://www2.ati.com/drivers/linux/amd-driver-installer-12-4-x86.x86_64.run) from [AMD](http://support.amd.com/us/gpudownload/linux/Pages/radeon_linux.aspx)
2. Extract the files from the package:
   `sh ./amd-driver-installer-12-4-x86.x86_64.run --extract ati`
3. Build your new ati/fglrx deb packages:
   `./ati-installer.sh 8.961 --buildpkg Ubuntu/precise`
4. Install our newly created deb packages:
   `sudo dpkg -i ../fglrx*.deb`
5. If your /etc/X11/xorg.conf is missing you will need to run:
   `sudo aticonfig --initial`
   and then reboot.

That newly created package should work for 3.2 kernel series in Precise.
