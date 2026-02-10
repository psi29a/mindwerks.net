---
date: 2007-06-01
categories:
  - Linux
  - Software
tags:
  - vmware
  - opensource
  - usb
  - issue
  - tip
  - Bret Curtis
---

# USB not showing up in VMware

For the longest time USB used to work quite well in VMware, then as if by magic, it all stopped working. However, after poking around I've discovered that there is a solution and it involves usbfs (usbdevfs). So here is a solution to get you all back up and running.

- Create a new user group and name it usbfs, let's say that it has gid 1003
- within /etc/fstab change the following line
`usbdevfs /proc/bus/usb usbfs noauto 0 0`- if you have it, change it to below, if you don't have it, then just add the following line
`usbfs /proc/bus/usb usbfs rw, devgid=1003, devmode=0640, busgid=1003, busmode=0550, listgid=1003, listmode=0440 0 0`- add vmware users to group usbfs
`usermod -G usbfs vmwareuser`- If you get an error like this:
`mount: mount point /proc/bus/usb does not exist` - then you have to compile a custom kernel from sources with CONFIG\_USB\_DEVICEFS enabled.
