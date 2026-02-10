---
date: 2008-02-27
categories:
  - Debian
  - Laptop
tags:
  - debian
  - laptop
  - dell
  - d505
  - latitude
  - wireless
  - xorg
  - linux
  - opensource
  - Bret Curtis
---

# Debian 4.0 on Dell Latitude D505

So tried my hand at getting Linux up and running on a hand me down laptop that I'll be doing a lot of work on. It is a Dell Latitude D505 with 1.2 Gigs of DDR ram, 1024x768 15in LCD, Pentium-M 1.5Ghz, Intel based wireless (802.11b), 120Gig Drive, and Intel based video card.

Started off wired to the Internet, Debian 3.1 install CD, linux26 install and everything was smooth sailing during install process. I selected http for getting my apt sources, wrapped up the install, rebooted. Once logged in, I immediately added testing and performed a aptitude dist-upgrade. This bumped me up to Debian 4.0. I installed the latest kernel 2.6.22 as it comes with the ipw2100 driver automatically. The earlier kernels do not and require you to compile yet more source code.
The first hurdle (and reason why Debian still isn't ready for your mum): Even though the ipw2100 module loads, it can't bring the wireless card online without a firmware. Well, you're in luck because someone out there is providing it for us but Debian won't do any of the work for you.
> <http://ipw2100.sourceforge.net/firmware.php>

Go there, agree to their EULA, and download the latest firmware. Unpack the contents into your /usr/lib/hotplug/firmware and you should be good to go.

By this time you may be wondering else you will need, so I suggest (because it works) to do a aptitude install wireless-tools which will make life a lot easier for you when setting up your wireless connection. Up to you have you want to do it, I installed gnome and had it's network tool handle everything.

Now if you are a road-warrior and gnome and iwconfig takes to long, there is another tool that you can use called Wicd.
> <http://wicd.sourceforge.net/>

It is simple stupid to install and use, works great and remembers your keys when you are hopping around. I only wish gnome's network tool was that smart. (Hint Gnome Devs)

Now, basically everything on the laptop works marvelously well, except the Lid issue. While in X (Xorg), if you close the lid the system will hang. I have the A11 bios update, which is known to cause all sorts of crap. I haven't yet had the chance to downgrade to A09 yet, but I may. A stupid hack around this is to dump to console (ctrl-alt-f1) and close the lid. When you want to go back, open lid and press (ctrl-alt-f7) to get back into X. If anyone else has suggestions to get past this, please let me know. I just want the LCD to go off and on when button is depressed.

So all in all, a success with a few minor flaws. I'll add more details as they creep into my mind.
