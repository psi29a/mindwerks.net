---
date: 2014-01-26
categories:
  - Code
  - C/C++
  - Linux
  - Windows
  - Software
tags:
  - WildMIDI
  - 0.3.2
  - midi
  - midi player
  - midi synthesizer
  - softsynth
  - software synthesizer
  - Chris Ison
  - Wildcode
  - psi29a
  - Bret Curtis
---

# Introducing WildMIDI version 0.3.2

![WildMIDI](../../assets/images/2014/01/WildMIDI.png){ align=left width="200" }

After several years of silence, There is now a new version of [WildMIDI](https://mindwerks.net/projects/wildmidi/ "WildMIDI")! Chris "Wildcode" Ison seems to have fallen off the planet around February of 2012 and the bug reports and patches have been accumulating on his [SourceForge](http://sourceforge.net/projects/wildmidi/) page. I decided to dump his [SVN repository](http://sourceforge.net/p/wildmidi/svn/HEAD/tree/) to [github](https://github.com/psi29a/wildmidi) and continue hacking where he left off. We are still very much 100% API/ABI compatible and new versions can be considered drop-in replacements. We will continue to be open to developers that wish to improve [WildMIDI](https://mindwerks.net/projects/wildmidi/ "WildMIDI") but keep in mind that our goal is to be small and fast. We also wish Chris the very best and want very much for him to rejoin the project.

**What's new?**

There have been a lot of changes since WildMIDI 0.2.3.5, mostly involving our new build system.

- Switched build system away from autotools and now using cmake
- We can build natively on: Linux, FreeBSD, Windows and OSX
- We support GCC, Clang, XCode and Visual Studio
- Pulled in all out-standing patches from SourceForge, Debian and FreeBSD
- Compile without warnings using enforced -Werrors
- Found and fixed additional bugs

**What we need**:
We still need people with other platforms to test [WildMIDI](https://mindwerks.net/projects/wildmidi/ "WildMIDI") and file [bug reports](https://github.com/psi29a/wildmidi/issues) and patches so that we can support more platforms as well. This includes both the library and the player.

We are also looking into adding new features, such as: XMI playback support, SF2 and DLS support.

**Downloads**:

- Win32 Binaries (exe, dll, lib): [WildMIDI-0.3.2-win32.zip](https://github.com/Mindwerks/wildmidi/releases/download/wildmidi-0.3.2/WildMIDI-0.3.2-win32.zip)
- OSX Binaries: Not currently available, they can be built from source but there is currently no sound-code for the wildmidi player. You can however dump music to a WAV file.
- Source: [wildmidi-0.3.2.tar.gz](https://github.com/psi29a/wildmidi/archive/wildmidi-0.3.2.tar.gz "WildMIDI 0.3.2")
- Free Patches (GUS):[freepats\_20060219.orig.tar.gz](http://ftp.de.debian.org/debian/pool/main/f/freepats/freepats_20060219.orig.tar.gz "freepats_20060219.orig.tar.gz") (extract the 'freepats' directory to where you want and adjust the 'dir' in wildmidi.cfg to point to it)

**For more information**:
If you wish to read more about the History and the Future of the library, please read our [WildMIDI Project](https://mindwerks.net/projects/wildmidi/ "WildMIDI") page.

**Screenshots running on Windows and Linux**:
