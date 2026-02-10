---
date: 2010-11-24
categories:
  - Laptop
  - Video
  - Ubuntu
tags:
  - 2.6.37
  - ati
  - fglrx
  - kernel
  - meerkat
  - narwhal
  - ubuntu
  - Bret Curtis
---

# Ubuntu 10.10 Maverick with 2.6.37 kernel

![glxgears](../../assets/images/2010/11/glxgears.png){ align=left width="200" }

If you want the latest (read bleeding edge) kernel that the Ubuntu developers are working, then have a look here:

[Ubuntu Dev Kernels](http://kernel.ubuntu.com/~kernel-ppa/mainline/)

Be sure to download the 3 files matching your architecture and install.

I am currently using 2.6.37-rc3-natty which will be the kernel that Natty Narwhal (11.04) will be based on. It just works, everything is detected and there is a noticeable increase in responsiveness.

Previously I posted about the 200~ kernel patch to increase desktop responsiveness. You do not need to wait for a new kernel or recompile one yourself to test the benefits. According to this [Linux kernel mailing list](http://thread.gmane.org/gmane.linux.kernel/1063263): While the correct way is to implement it in kernel to be transparent to the user, you can enable it with a few quick entires in to your ~/.bashrc file.
`if [ "$PS1" ] ; then
mkdir -m 0700 /sys/fs/cgroup/cpu/user/$$
echo $$ > /sys/fs/cgroup/cpu/user/$$/tasks
fi`

Then, as the superuser do this:
 `mount -t cgroup cgroup /sys/fs/cgroup/cpu -o cpu
mkdir -m 0777 /sys/fs/cgroup/cpu/user`

"Done. Same effect. However: not crazy."

Thank you Lennart.
