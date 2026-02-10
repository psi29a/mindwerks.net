---
date: 2010-03-31
categories:
  - Laptop
  - Ubuntu
tags:
  - laptop
  - ubuntu
  - studio xps
  - dell
  - 1640
  - xorg
  - dual-screen
  - ati
  - fglrx
  - Bret Curtis
---

# Ubuntu Karmic 9.10 on Dell Studio XPS 1640

The very first thing I did when the company I work for gave me a laptop, a Dell Studio XPS 1640, was to install Ubuntu Karmic on it. No need for windows on this thing, I plan on working, not playing.

![karmic 9.10](../../assets/images/2010/03/karmic9-101.png){ align=left width="200" }

Dell is very good about their laptops. Whenever I had a question, everything I ever needed to know about their hardware I could easily look up on the online. The 1640 is no exception with their [manual](http://support.dell.com/support/edocs/systems/sxl1645/en/sm/index.htm "Dell Studio XPS 16 Manual").
**The setup:**

- ﻿Intel Core2 Duo: T7350
- 4GB of DDR3 ram
- ﻿﻿﻿Radeon Mobility HD 3670
- RV635 Audio device
- Intel Corporation Wireless WiFi Link 5100
- BCM5784M Gigabit Ethernet
- Intel 82801I (ICH9 Family) Chipset
- Intel ICH9M/M-E SATA AHCI Controller
- WesternDigital WD3200BJKT-7 320GB Harddriver
- TSSTcorp DVD+/-RW TS-T633A, D600

**Key Elements:**

- Ubuntu Karmic 9.10
- typical development setup (build-essentials)
- Skype
- fglrx
- Virtualbox
- ext4 filesystem

The install happened in September 2009, but I felt it best to share what I went through before going to Ubuntu Lucid 10.04. The install itself went without a problem, everything loaded up fine.
At the time, I was using the 'ati' xorg driver. I attached a separate monitor (Dell 23") and configured it using the Display Preferences tool to be one big desktop. This gets a little weird with one monitor being 1920x1080 and the laptop LCD at 1366x768 but what happens is that it creates a virtual desktop size that covers both screens with a little cut-off at the bottom (or top) of the laptop LCD screen.
I wanted to switch over to the fglrx driver for it's 3D acceleration but immediately came into a problem in that my screen setup above would just not work. I hunted through forums and documentation but eventually with some guess work, I managed to get the big virtual desktop setup and fglrx to work together.
Here is my modified: /etc/X11/xorg.conf

```
Section "Monitor"
	Identifier     "Monitor0"
	VendorName     "Unknown"
	ModelName      "DELL S2309W"
	HorizSync       30.0 - 83.0
	VertRefresh     50.0 - 76.0
	Option         "DPMS"
EndSection

Section "Monitor"
	Identifier     "Monitor1"
	VendorName     "Unknown"
	ModelName      "LCD"
	HorizSync       30.0 - 83.0
	VertRefresh     50.0 - 76.0
	Option         "DPMS"
EndSection

Section "Screen"
	Identifier	"Configured Screen Device"
	Device	"Configured Video Device"
	DefaultDepth	24
	SubSection "Display"
		Virtual	3840 2160
	EndSubSection
EndSection

Section "Module"
	Load	"glx"
EndSection

Section "Device"
	Identifier	"Configured Video Device"
	Driver	"fglrx"
	Option "AccelMethod" "exa"
EndSection

Section "ServerFlags"
	Option "RandR" "on"
EndSection>
```

The benefit of this setup is that I was then able to turn on compiz for a compositing windows manager. I use normal, I do not need the flashy effects.
System->Preferences->Appearance->Visual Effects->Normal
It worked seamlessly across the two screens and the openGL programs worked flawlessly.
So there you are, everything worked out of the box on the laptop except for the ability to have an additional monitor. Even that was fixed with a bit of hacking.
Aside from it's looks, it is a very nice desktop replacement. Everything just simply works.
