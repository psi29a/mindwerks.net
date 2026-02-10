---
date: 2010-09-30
categories:
  - Laptop
  - Video
  - Ubuntu
tags:
  - xorg
  - fglrx
  - unstable
  - ati
  - Bret Curtis
---

# xorg 1.9 versus fglrx

With the release of Ubuntu (Meerkat) 10.10 just 10 days away, the [ubuntu x-swat](https://launchpad.net/~ubuntu-x-swat) people have been busy getting fglrx ready for release. The fglrx now compiles against latest Meerkat kernel and finally resolves the unknown symbol issue.

![xswat-64](../../assets/images/2010/09/xswat-64.png){ align=left width="64" }

In the laptop is a ATI Mobility Radeon HD 3670 and with the latest fglrx driver usability is awful. There is horrible tearing when using "Appearance -> Visual Effects -> Normal", which had to be set back to "None" just to be usable. Even on "None", scrolling down in documents, chrome, firefox and Skype all give blurred or stuttered graphics.

These are for me "do not use" releases.

There are so far two updates. The first one gets fglrx up to date to latest Meerkat.
> fglrx-installer (2:8.780-0ubuntu1) maverick; urgency=low
> \* New upstream release.
> - Fix build issues with kernel fix for CVE-2010-3081 (LP: #642518).
> - Add compatibility with 2.6.35 kernels (LP: #573748).
> - Add compatibility with xserver 1.9 (LP: #630599).
> \* Make the driver Depend on the appropriate xserver-xorg-video-$ABI
> (LP: #616215).

The latest update adds 2.6.36 kernel support:
> fglrx-installer (2:8.780-0ubuntu2) maverick; urgency=low
> \* debian/fglrx.postinst:
> - Call dpkg-trigger with "--by-package".
> \* Add add-compatibility-with-2.6.36-kernels.patch:
> - Fix build issues with 2.6.36 kernels.
> \* Add use-cflags\_module-together-with-modflags.patch:
> - Fix build issues with kernels that don't have
> MODFLAGS and use CFLAGS\_MODULE.

There will hopefully be more releases soon that help to resolve these issues
