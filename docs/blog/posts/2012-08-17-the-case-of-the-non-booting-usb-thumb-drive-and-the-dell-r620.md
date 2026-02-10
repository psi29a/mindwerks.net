---
date: 2012-08-17
categories:
  - Hardware
  - Servers
  - Linux
tags:
  - dell
  - r620
  - usb
  - Bret Curtis
---

# The case of the non-booting USB thumb-drive and the Dell R620

![dell_poweredge_r620](../../assets/images/2012/06/dell_poweredge_r620.jpg){ align=left width="200" }

Awhile back I wrote about '[Doing battle with a Dell R620 and Ubuntu](https://mindwerks.net/2012/06/doing-battle-with-a-dell-r620-and-ubuntu/ "Doing battle with a Dell R620 and Ubuntu")' where I touched on the fact that booting from USB thumb-drive was a painful problem. In short, the same USB thumb-drive that would work in the R610 would not work in the R620.

It comes down BIOS support for USB and how it is handled. On the R610 there are 3 options: 'auto-detect', 'floppy emulation' and 'hard drive'. Auto was hit-or-miss, floppy would not work but 'hard drive' worked every time. On the R620 there are no options so I can only suppose that it supports 'floppy emulation' upon detection of a USB thumb-drive.

To try to find the cause of this problem we tried using the 'standard' method of taking Precise 12.04 ISO from Ubuntu's website and using UNetbootin to create a USB thumb-drive that did boot on the R620. It turns out there was something wrong with our process that prevented it from booting. In comparing the partition table (with parted) of our USB thumb-drive and the Precise thumb-drive we noticed that the starting position of the first (and only) partition were different!

Non-booting USB:
> Model: TDKMedia Trans-It Drive (scsi)
> Disk /dev/sdc: 3999MB
> Sector size (logical/physical): 512B/512B
> Partition Table: msdos

Number Start End Size Type File system Flags
1 1049kB 3998MB 3997MB primary ext4 boot

Booting USB:
> Model: TDKMedia Trans-It Drive (scsi)
> Disk /dev/sdc: 3999MB
> Sector size (logical/physical): 512B/512B
> Partition Table: msdos

Number Start End Size Type File system Flags
1 32.9kB 3998MB 3997MB primary ext4 boot

The choice to do 1MiB was to increase the lifespan of the thumb-drive by aligning the partition to the erase-block size of the thumb-drive. Doing this however renders 'floppy emulation' a non-option on both the Dell R620 and R610. Setting it to 32.9KiB also means that the drive is not properly aligned and you will get bad performance when writing, reading and health of the thumb-drive itself.

In the interest of getting bootable thumbdrive we ended up doing this:
`parted -a none /dev/sdb 'mkpart primary 0 -1 set 1 boot on'`
What this does is create a primary partition at the start of the thumb-drive that goes all the way to the end. We ignore the alignment problems and set the partition to bootable. After that, it was easy enough to through our ext4 filesystem on top and syslinux/casper to get our custom installer working.

The end result is that we now have a USB thumb-drive that boots on a R620 every time.
