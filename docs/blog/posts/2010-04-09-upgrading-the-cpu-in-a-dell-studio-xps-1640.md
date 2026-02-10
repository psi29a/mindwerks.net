---
date: 2010-04-09
categories:
  - Linux
  - Laptop
tags:
  - VT
  - laptop
  - studio xps
  - dell
  - cpu
  - upgrade
  - vt-x
  - vtx
  - processor
  - Bret Curtis
---

# Upgrading the CPU in a Dell Studio XPS 1640

While the default Dell Studio XPS 1640 is fast and is a decent work laptop, it needed to do one extra thing, run virtual machines (VMs). I spend a lot of my time debugging, hacking and otherwise trying to make software behave in ways that the developers had not intended.

Tools like VirtualBox, VMWare, Xen and QEMU make this job less tedious. The problem is that with the Intel T7350 CPU, I cannot run 64 bit VMs. Turns out that T7250 is a 64 capable chip, but without the VT-x extension which allows for hardware assisted virtualization.

Look your [Intel CPU](http://en.wikipedia.org/wiki/X86_virtualization#Intel_Virtualization_Technology_for_x86_.28Intel_VT-x.29) up to see if it supports the VT-x flag.
It turns out upgrading your CPU is relatively easy as Dell did a good job in designing the laptop. The instructions are all in their online [service manual](http://support.dell.com/support/edocs/systems/sxl1645/en/sm/index.htm).

[Replacing CPU in a Dell Studio XPS 1640](http://support.dell.com/support/edocs/systems/sxl1645/en/sm/cpucool.htm#wp1084976)

The only hard part is figuring out what CPU is compatible and then buying it. Thankfully my company had no problem ordering an upgrade and after the first successful attempt, they ordered more for my other colleagues as well.

When picking an upgrade CPU, you must find one your motherboard supports. Your best and most compatible guess is to choose one in the same family as your own CPU, essentially a later model. Since the [T7350](http://processorfinder.intel.com/details.aspx?sSpec=SLB53) has a 1066 front side bus (FSB) , 45nm process and takes 25W, it is then easy to find a similar CPU with those values but at a much higher clock rate and L2 cache, and most importantly, VT-x flag.

[Wikipedia](http://en.wikipedia.org/wiki/X86_virtualization#Intel_Virtualization_Technology_for_x86_.28Intel_VT-x.2) has a list of all mobile processors that have the VT-x flag.
> - Mobile Core 2 Duo T5500, T5600, T6670, T7100, T7200, T7250, T7300, T7400, T7500, T7600G, T7700, T7800, U7500, L7200, L7300, L7400, L7500, L7700, U7500, U7600, U7700 (Merom)
> - Mobile Core 2 Duo SU7300, SU9300, SU9400, SU9600, SL9300, SL9380, SL9400, SL9600, SP9300, SP9400, SP9600, P7350 (mac),P7370, P7550 (confirmed), P7570, P8400, P8600, P8700, P8800, P9500, P9600, P9700, T8100, T8300, T9300, T9400, T9500, T9550, T9600, T9800, T9900 (Penryn)

A successor of the T7350 (Merom-2M) is the P8700 (Penryn-3M) and fits all my requirements to fit in the laptop. It is faster and more importantly has the VT-x flag and is easily found online for very cheap.

The installation went without incident and upon reboot I entered the BIOS and enabled the "Hardware Virtualization" option. Saved and rebooted, Virtualbox finally gave me the option to create and run 64-bit VMs.

*An additional note*: Updating (Flashing) the BIOS is not necessary. The BIOS checks to see if the CPU has the flag or not and will not display the "Hardware Virtualization" option if the CPU does not support it.
