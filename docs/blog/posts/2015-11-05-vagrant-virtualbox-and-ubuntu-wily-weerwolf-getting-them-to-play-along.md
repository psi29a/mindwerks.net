---
date: 2015-11-05
categories:
  - Software
  - Ubuntu
tags:
  - 15.10
  - libvpx
  - ubuntu
  - Vagrant
  - VBox
  - VirtualBox
  - Weerwolf
  - Wily
---

# Vagrant, Virtualbox and Ubuntu Wily Weerwolf: Getting them to play along

![Vagrant](../../assets/images/2015/11/Vagrant.png){ align=left width="200" }

I recently upgraded to Ubuntu 15.10 (Wily Weerwolf) which automatically upgraded VirtualBox from 4.3 to 5.0 and broke compatibility with Vagrant 1.6 in the process. Thinking that Vagrant knows about this and they claim VBox 5.0 compatbility, I upgraded to 1.7 and came across the same error!

> [Vagrant attempted to execute the capability ‘configure\_networks’ on the detect guest OS ‘linux’](https://github.com/mitchellh/vagrant/issues/6426)

There is a workaround!

Apparently it hasn’t been fixed yet and others are also running into this problem. Being pragmatic, I reverted Vagrant back to 1.6 and purged VirtualBox from my system. I manually downloaded an older 4.3 build of VBox from here: https://www.virtualbox.org/wiki/Download\_Old\_Builds\_4\_3

Of course these builds are only supported up to Ubuntu 14.10, so we have a bit more work to get back to work. The first bit is that the VBox deb package won’t install until ***libvpx1*** is installed. The problem here is that this package no longer exists in Ubuntu 15.10, but it’s later revision libvpx2 does. So we have to create a temporary empty deb package to allow installation without forcing anything.

You can follow the directions here to create your own package here: [Creating\_dummy\_packages\_to\_fullfill\_dependencies\_in\_Debian](https://www.brain-dump.org/blog/entry/40/Creating_dummy_packages_to_fullfill_dependencies_in_Debian).

Or you can download it from me here: [libvpx1\_1.0.0\_all.deb](https://web.archive.org/web/20170920181652/https://www.mindwerks.net/wp-content/uploads/2015/11/libvpx1_1.0.0_all.deb)

Now you can install your VBox 4.3 without it complaining. However if you try to do this:

> `vagrant up`

You’ll get this:

> Bringing machine ‘default’ up with ‘virtualbox’ provider…  
> There was an error while executing `VBoxManage`, a CLI used by Vagrant  
> for controlling VirtualBox. The command and stderr is shown below.
>
> Command: [“list”, “hostonlyifs”]
>
> Stderr: VBoxManage: error: Failed to create a session object!  
> VBoxManage: error: Code NS\_ERROR\_FACTORY\_NOT\_REGISTERED (0x80040154) – Class not registered (extended info not available)  
> VBoxManage: error: Most likely, the VirtualBox COM server is not running or failed to start.

This is solved by making a symlink from ***libvpx.so.2*** to ***libvpx.so.1*** and it should be solved. We’re back to normal, until the original problem with Virtualbox 5.0 and Vagrant are fixed.
