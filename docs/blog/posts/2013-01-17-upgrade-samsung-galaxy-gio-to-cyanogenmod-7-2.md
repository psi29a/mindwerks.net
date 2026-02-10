---
date: 2013-01-17
categories:
  - Mobile
  - Linux
tags:
  - 2.3
  - android
  - brick
  - gingerbread
  - gio
  - samsung
  - samsung gio
  - cyanogenmod
  - 7.2
  - cyanogenmod 7.2
  - phiexz
  - Bret Curtis
---

# Upgrade Samsung Galaxy Gio to CyanogenMod 7.2

![Android](../../assets/images/2012/08/android-logo.gif){ align=left width="200" }

Going from 2.3.x (Gingerbread) to [CyanogenMod](http://en.wikipedia.org/wiki/CyanogenMod "CyanogenMod") 7.2 (Gingerbread) is surprisingly simple unlike upgrading from Froyo. I'll go into more detail below, but there are two necessary bits: an updated recovery rom and a custom (non-official) CyanogenMod rom. This version of CyanogenMod is specific to the [Samsung Gio](http://wiki.cyanogenmod.org/index.php?title=Unofficial_Ports#Samsung_Galaxy_Gio_.28GT-S5660.29 "cyanogenmod samsung gio").

Before upgrading your Samsung Gio, you must first be running at least 2.3.x (Gingerbread) before continuing because of the use of ext4 instead of rfs. Please follow my upgrade guide "[Upgrade Samsung Galaxy Gio from 2.2.x Froyo to 2.3.x Gingerbread](https://mindwerks.net/2012/08/upgrade-samsung-galaxy-gio/ "Upgrade Samsung Galaxy Gio from 2.2.x Froyo to 2.3.x Gingerbread")" first.

**Warning:** *Caveat emptor* - While I used to this process to update my phone, I take no responsibility if you brick your phone. Be sure to back up anything you wish to save, this procedure works best when your Gio is fully wiped of data.

**Installation of the ClockworkMod (CWM)**

1. Download the custom CWM "[px-cwm-v2.zip](http://www.mindwerks.net/wp-content/uploads/custom/px-cwm-v2.zip "ClockworkMod ")" and copy it to your sdcard.
2. Reboot into the default recovery in your stock Gingerbread or with your Gio turned off, hold down the Home/OK (middle) button and press the Power button.
3. In recovery mode, use the Volume buttons for navigation and the Home/OK button for selecting.
4. Select “Update from SD card” from the recovery menu.
5. Look for "px-cwm-v2.zip" which should be on your sdcard and press OK to flash.
6. Reboot again like above into recovery mode and you should now have the new CWM recovery screen.

You can read more about CWM [here](http://www.addictivetips.com/mobile/what-is-clockworkmod-recovery-and-how-to-use-it-on-android-complete-guide/).

Here is a video that shows the process:
http://www.youtube.com/watch?feature=player\_embedded&v=hxjxB8P9rSU

**Installation of CyanogenMod 7.2 for Samsung Gio**

1. Download *update-cm-7.2.0-20120710-NIGHTLY-gio-AROMA.zip* from either [here](http://www.mediafire.com/?dyfx3xb03s8402b "update-cm-7.2.0-20120710-NIGHTLY-gio-AROMA.zip") or [here](https://www.dropbox.com/s/48o7axrvtb451rk/update-cm-7.2.0-20120710-NIGHTLY-gio-AROMA.zip "update-cm-7.2.0-20120710-NIGHTLY-gio-AROMA.zip").
2. Copy to sdcard
3. Reboot to Recovery Mode (CWM)
4. Select install zip from sd card
5. Select "update-cm-7.2.0-20120710-NIGHTLY-gio-AROMA.zip" ROM
6. Select Yes - Install update
7. Wait till the Installation is finish
8. Select wipe data/factory reset
9. Select reboot mobile and enjoy

**Cyanogen Mod 7.2.0 For Galaxy Gio based on Gingerbread (2.3.7)**
*Working:*

- RIL
- proximity sensor
- touchscreen with multi touch
- keychar
- storage mode
- gps
- compass
- accelerometer sensor
- microphone (both phone & headset)
- headset button
- Root & Busybox
- call,sms,mms
- auto rotate
- packet data with automatically apn detect
- GPRS, EDGE, 3G, HSDPA
- wifi
- hardware video acceleration
- secret code
- bluetooth
- camera
- static wifi mac address
- audio & FM Radio
- wired & hotspot tether
- Backlight Notification

*Not Working:*

- Sim Toolkit (maybe)

*Known issues:*

- some option are not working on setting (like: mute camera sound, etc)
- slow loading png image on gallery
- after use camera, governor force back to "ondemand"

*Sources:*

- <https://github.com/phiexz>
- [http://android.phiexz.com/](https://github.com/phiexz)

All thanks should go to CyanogenMod team, phiexz and all those that have put effort into ever aspect of this ROM.

**This is part 2 of a 3 part series about the Galaxy Gio.**
Part1: [Upgrade Samsung Galaxy Gio from 2.2.x Froyo to 2.3.x Gingerbread](https://mindwerks.net/2012/08/upgrade-samsung-galaxy-gio/ "Upgrade Samsung Galaxy Gio from 2.2.x Froyo to 2.3.x Gingerbread")
Part2: [Upgrade Samsung Galaxy Gio to CyanogenMod 7.2](https://mindwerks.net/2013/01/upgrade-samsung-galaxy-gio-to-cyanogenmod-7-2/ "Upgrade Samsung Galaxy Gio to CyanogenMod 7.2")
Part3: [Upgrade Samsung Galaxy Gio to CyanogenMod 10.1](https://mindwerks.net/2013/05/upgrade-samsung-galaxy-gio-to-cyanogenmod-10-1/ "Upgrade Samsung Galaxy Gio to CyanogenMod 10.1")
