---
date: 2014-06-13
categories:
  - C/C++
  - Software
  - Code
tags:
  - midi
  - patches
  - softsynth
  - sound fonts
  - synthesizer
  - WildMIDI
  - xmi
  - mus
  - hmi
  - hmp
  - Bret Curtis
---

# WildMIDI 0.3.7 has been released

![WildMIDI](../../assets/images/2014/01/WildMIDI.png){ align=left width="200" }

We're still quite busy with developing 0.4 and thought it was best to backport our fixes into the 0.3 branch. As a result we ended up having an additional 2 releases in the 0.3 branch!

**What's new in this release**

We've added DOS support in the form of SoundBlaster 16 playback in the player. The other big surprise is MIDI type-2 support, which came as a by-product of fully supporting XMI files like those from [The Legend of Kyrandia](https://en.wikipedia.org/wiki/The_Legend_of_Kyrandia "The Legend of Kyrandia"). The rest of the changes are further enhancements to our build system and bug-fixes.

**What to look forward to...**:

We've wrapped up XMI (Eye of the Beholder 3) and Id's MUS (Doom, Raptor) support (with change of frequency support). We also have some preliminary support for playback of HMI (Daggerfall, X-COM) and HMP (Descent, Abuse) files! We are also working with the community and sharing our results, in response, they (to yet be named) are going to re-license their research and code to be more compatible with WildMIDI! This will certainly make engine re-implementation work easier for those that wish to use the library playback music. This is all being worked on currently in the 0.4 branch.

If you are interested in helping out, please leave a comment or fork the code on github! We're always looking at supporting more MIDI like formats.

***The full change log***:

- Plug a memory leak in case of broken midis.
- Properly reset global state upon library shutdown.
- Support for type-2 midi files.
- Fix a possible crash in WildMidi\_SetOption.
- DOS port: Support for Sound Blaster output in player.
- Uglify the library's private global variable and function names.
- Build: Add option for a statically linked player.
- Build: Add headers to project files. Use -fno-common flag.
- Other small fixes/clean-ups.
- Fix some portability issues.
- Fix a double-free issue during library shutdown when several midis were alive.
- Fix the invalid option checking in WildMidi\_Init().
- Fix the roundtempo option which had been broken since its invention in 0.2.3.5 (WM\_MO\_ROUNDTEMPO: was 0xA000 instead of 0x2000.)
- Fix cfg files without a newline at the end weren't parsed correctly.
- Handle cfg files with mac line-endings.
- Refuse loading suspiciously long files.

**Downloads**
Source and binaries can be found on our github release page:
[https://github.com/Mindwerks/wildmidi/releases](https://github.com/Mindwerks/wildmidi/releases "WildMIDI Releases")
