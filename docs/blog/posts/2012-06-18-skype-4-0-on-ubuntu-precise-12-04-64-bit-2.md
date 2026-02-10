---
date: 2012-06-18
categories:
  - Ubuntu
  - Software
tags:
  - ubuntu
  - 12.04
  - LTS
  - skype
  - Bret Curtis
---

# Skype 4.0 on Ubuntu Precise (12.04) 64-bit

![skype](../../assets/images/2011/09/skype.png){ align=left width="200" }

There is a new version of skype out for Linux, version 4.0 which has interesting [changelog](http://blogs.skype.com/linux/2012/06/skype_40_for_linux.html) entries:
> \* Much lower chance Skype for Linux will crash or freeze
> \* chat history loading is now much faster
> \* ...several investments we made in improving audio quality ... and improving video call quality
> \* ...extended support for more cameras
> \* and more

Good enough for me! There is still no true 64 bit binary/package from Skype. The result is that their fake "64 bit" Skype needs an additional 100MB of i386 packages in order for it to run properly.
The rundown:

1. Remove old skype packages if they exist: `sudo apt-get purge skype skype-bin`
2. Download latest [Skype (4.0)](http://www.skype.com/intl/en/get-skype/on-your-computer/linux/downloading.ubuntu64) (fake) 64-bit package for Ubuntu 10.04+. It might say skype 2.2 beta on the screen, they have yet to update the page. The download link goes to the 4.0 version.
3. Install the necessary support libraries: `sudo apt-get install ia32-libs lib32stdc++6 lib32asound2`
4. Install the skype binary package itself: `sudo dpkg -i skype-ubuntu_4.0.0.7-1_amd64.deb`

Enjoy the ad-free Linux version of Skype thanks to... Microsoft.
