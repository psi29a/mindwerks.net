---
date: 2015-05-07
categories:
  - Ubuntu
  - Linux
  - Operating Systems
  - RaspberryPi
  - Hardware
  - C/C++
  - Code
tags:
  - Bret Curtis
  - Arm
  - VC4
  - compile
  - cross-compile
  - kernel
  - linux
  - Raspberry Pi 2
  - Raspberry Pi
  - RPi2
  - RPi
---

# Cross-compiling for Raspberry Pi on Ubuntu

![RaspberryPi Logo](../../assets/images/2014/08/RaspberryPi_Logo.png){ align=left width="200" }

While the Raspberry Pi 2 has four cores to churn through code, it still takes longer to compile than on most workstations and laptops. If you are feeling adventurous, you can try cross-compiling which has become easier to set up and get working.
Cross-compiling is when binaries created are for another target architecture than the one you are compiling on. This kind of set up is very typical when creating Android applications. The end result is that you can take the resulting binary and place on its target platform, and it will run there.
There are even tricks to getting the cross-compiled binary to also run on your native system!
In this guide, I'll walk you through:

- Setting up a cross-compile toolchain in Ubuntu (15.04 Vivid)
- Setting up the proper exports
- Compiling a test program for your native and target armhf platform
- Compiling the latest Raspberry Pi 2 kernel with VC4 support.

The first thing we need to do is set up your Ubuntu to be able to compile software for a Raspberry Pi (1 and 2). You'll need at least Ubuntu Vivid (15.04) installed. From there, you'll need to install the following packages.

```
sudo apt-get install binutils-arm-linux-gnueabihf \
cpp-4.9-arm-linux-gnueabihf \
cpp-arm-linux-gnueabihf \
g++-4.9-arm-linux-gnueabihf \
g++-4.9-multilib-arm-linux-gnueabihf \
g++-arm-linux-gnueabihf \
gcc-4.9-arm-linux-gnueabihf \
gcc-4.9-arm-linux-gnueabihf-base \
gcc-4.9-multilib-arm-linux-gnueabihf \
gcc-arm-linux-gnueabihf \
pkg-config-arm-linux-gnueabihf \
binutils-arm-linux-gnueabihf \
cmake \
cpp-4.9-arm-linux-gnueabihf \
cross-gcc-dev \
dpkg-cross \
g++-4.9-arm-linux-gnueabihf \
g++-4.9-multilib-arm-linux-gnueabihf \
gcc-4.9-arm-linux-gnueabihf \
gcc-4.9-arm-linux-gnueabihf-base \
gcc-4.9-multilib-arm-linux-gnueabihf \
libasan1-armhf-cross \
libatomic1-armhf-cross \
libc6-armel-armhf-cross \
libc6-armel-cross \
libc6-armhf-cross \
libc6-dev-armel-armhf-cross \
libc6-dev-armel-cross \
libc6-dev-armhf-cross \
libdebian-dpkgcross-perl \
libfile-homedir-perl \
libgcc-4.9-dev-armhf-cross \
libgcc1-armhf-cross \
libgomp1-armhf-cross \
libsfasan1-armhf-cross \
libsfatomic1-armhf-cross \
libsfgcc-4.9-dev-armhf-cross \
libsfgcc1-armhf-cross \
libsfgomp1-armhf-cross \
libsfstdc++-4.9-dev-armhf-cross \
libsfstdc++6-armhf-cross \
libsfubsan0-armhf-cross \
libstdc++-4.9-dev-armhf-cross \
libstdc++6-armhf-cross \
libubsan0-armhf-cross \
linux-libc-dev-armhf-cross \
pdebuild-cross \
xapt \
```

The last package in the list is xapt, a wrapper around apt so that we can install packages specifically for other architectures like `armhf`. This includes things like \*-dev packages with headers which will likely be required if you compile other software.
Once those are installed, you need to tell the terminal you are targeting the `armhf` architecture. The CROSS\_COMPILE flag will make your toolchain (gcc and friends) and your software aware that you are using a cross-compiler.

```
export $(dpkg-architecture -aarmhf) 
export CROSS_COMPILE=arm-linux-gnueabihf-
```

You might get this warning:
> dpkg-architecture: warning: specified GNU system type arm-linux-gnueabihf does not match gcc system type x86\_64-linux-gnu, try setting a correct CC environment variable

This message is harmless and you can ignore it.
Now to test this, create a file called `main.c` and copy this Hello World code into it.

```
#include <stdio .h>
#include <stdlib .h>

int main(int argc, char **argv)
{
    printf("Hello world\
");
}
```

You'll then compile it twice, first natively and second for your target platform.

```
gcc -o hello_x86 main.c -static
arm-linux-gnueabihf-gcc -o hello_arm main.c -static
```

You can then use `file` to test the resulting output and it should match below:
> bcurtis@Redqueen:~/workspace/RPi$ file hello\_x86
> hello\_x86: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, for GNU/Linux 2.6.32, BuildID=217c28644cf5be3ea4d24bea79c3da3bbdd9a2a9, not stripped
> bcurtis@Redqueen:~/workspace/RPi$ file hello\_arm
> hello\_arm: ELF 32-bit LSB executable, ARM, EABI5 version 1 (GNU/Linux), statically linked, for GNU/Linux 2.6.32, BuildID=3a5e42174d6b72ddf8b0265a9b76b3cea0668623, not stripped

Notice how the last one is `ARM, EABI5 version 1`, this indicates that the binary is compiled for armhf, your Raspberry Pi. Next we are going to try to run them:
> bcurtis@Redqueen:~/workspace/RPi$ ./hello\_x86
> Hello world
> bcurtis@Redqueen:~/workspace/RPi$ ./hello\_arm
> Hello world

You might asking you how the `hello_arm` binary can run on an x86 system. This is thanks to `-static` flag during compilation that shoves all the required libraries into your binary. The ones that you included are specifically crafted multi-libs that can used on both your host and your target platform (both x86 and arm). The resulting binaries are larger as a result. You can remove the `-static` flag and see that it will no longer run on your host machine, but much smaller and will run on your target RPi2.
Aiming higher, we will try to get Linux kernel built using Eric Anholt's VC4 branch. Go ahead and checkout Eric's branch: <https://github.com/anholt/linux/tree/vc4-kms-v3d-rpi2>

```
git clone git@github.com:anholt/linux.git -b vc4-kms-v3d-rpi2 --depth 10
cd linux
export $(dpkg-architecture -aarmhf); export CROSS_COMPILE=arm-linux-gnueabihf-
make ARCH=arm -j`nproc` bcm2709_defconfig
make ARCH=arm -j`nproc`
```

It will spawn a number of processes in parallel, `nproc` will return back how many cores you have. After a few minutes of tea sipping, you'll have your newly minted `arch/arm/boot/zImage` that you can then copy over to your sdcard. Take a moment to make sure your setup.cfg is pointing to the right kernel, then give it a try. You should now have your RPi2 online with Linux 4.0!
Please note, at the time of this post, while the option to compile in VC4 support is there, it currently isn't functioning. Eric is still busy getting RPi2 back to the same state as the original RPi. Cheers!
