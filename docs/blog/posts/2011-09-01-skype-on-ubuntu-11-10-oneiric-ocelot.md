---
date: 2011-09-01
categories:
  - Ubuntu
  - Software
tags:
  - skype
  - ubuntu
  - multiarch
  - 64
  - x86
  - 11.10
  - Oneiric Ocelot
  - Bret Curtis
---

# Skype on Ubuntu 11.10 (Oneiric Ocelot)

![skype](../../assets/images/2011/09/skype.png){ align=left width="200" }

If you upgrade to Ubuntu 11.10 on a 64-bit platform and try to run skype then you will likely get this error:

> skype: error while loading shared libraries: libXss.so.1: cannot open shared object file: No such file or directory

This is because libxss1 and a few other libraries have been removed from ia32-libs package.

You will need to enable multiarch and install the extra 32 bit libraries by hand:
`echo foreign-architecture i386 | sudo tee /etc/dpkg/dpkg.cfg.d/multiarch
sudo aptitude update
sudo aptitude install libxss1:i386 libqtcore4:i386 libqt4-dbus:i386`

This is all that is required to get the statically compiled version of [Skype](http://www.skype.com/go/getskype-linux-beta-static) to work.

If you are running the dynamically compiled version or one that comes from mediabuntu or other source, you will need to pull in an extra package.
`sudo aptitude install libqtgui4:i386`

However, in my experience this pulls in too many unnecessary packages and some of them may be broken.

Update: I've done a fresh install of Oneiric and determined the following list of packages that need to be install to get skype working. In the mean time, please bug/pester Skype for real 64bit binaries.

`sudo aptitude install libxss1:i386 libqtcore4:i386 libqt4-dbus:i386 libasound2:i386 libxv1:i386 libsm6:i386 libxi6:i386 libXrender1:i386 libxrandr2:i386 libfreetype6:i386 libfontconfig1:i386`
