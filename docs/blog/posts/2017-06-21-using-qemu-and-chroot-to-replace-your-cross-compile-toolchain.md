---
date: 2017-06-21
categories:
  - Code
  - Debian
  - Linux
  - RaspberryPi
  - Software
tags:
  - arm64
  - chroot
  - compile
  - debian
  - linux
  - qemu
  - Raspberry Pi
  - toolchain
---

# Using Qemu and Chroot to replace your cross-compile toolchain

![RaspberryPi Logo](../../assets/images/2014/08/RaspberryPi_Logo.png){ align=left width="200" }

Awhile back I wrote about how you can set up a [cross-compile toolchain for compiling on x86\_64 with the Raspberry Pi](https://www.mindwerks.net/2015/05/cross-compiling-for-raspberry-pi-on-ubuntu/) as a target. There is another, perhaps easier way to do the same thing by using Qemu 2.0 as your backend.

By installing and enabling Qemu support, you can run code compiled for another architecture (that is supported by Qemu) on your native machine. You can then create a Chroot environment, perhaps similar to what you have on your Raspberry Pi, and run it as if it was natively.

You can verify support by checking for the availability of the aarch64 interpreter:  
`# update-binfmts --display | grep -i aarch  
qemu-aarch64 (enabled):  
interpreter = /usr/bin/qemu-aarch64-static`

**First you’ll need to set up your locales on your host:**  
You’ll need to configure locales so your Qemu Chroots have access to them. Otherwise, you will have to configure each Chroot’s locale individually.

`# From the host  
sudo dpkg-reconfigure locales`

**Secondly you’ll need to install the necessary packages:**  
This includes qemu, Chroot and binfmt support  
`# From the host  
sudo apt-get install qemu qemu-user-static binfmt-support debootstrap`

**Thirdly we create the Chroot.**  
This uses debootstrap to create the Chroot environment. In the command below, the Chroot will be named debian-arm64. You can change it to suit your taste.

# From the host

sudo qemu-debootstrap –arch=arm64 –keyring /usr/share/keyrings/debian-archive-keyring.gpg \  
–variant=buildd –exclude=debfoster stretch debian-arm64 http://ftp.debian.org/debian  
…  
I: Retrieving Release  
I: Retrieving Release.gpg  
I: Checking Release signature  
…

**Fourthly we step into Chroot**  
Lastly before it’s usable we’ll setup the guest environment.

`# From the host  
sudo chroot debian-arm64/`

apt-get install debian-ports-archive-keyring

apt-get install locales build-essential git curl cmake # and etc.

**Lastly…**  
The sky is the limit, you have your own chroot using binaries compiled for another arch. Clone your git repo, run cmake, install deps as necessary and run make to compile. The resulting binaries should run just fine on your RPi3.
