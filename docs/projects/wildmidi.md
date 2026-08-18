# WildMIDI: A Software Synthesizer

![WildMIDI](../assets/images/2014/01/WildMIDI.png){ align=left width="200" }

WildMIDI is a simple software midi player which has a core software synthesizer (softsynth) library that can be use with other applications.

**A bit of history**

WildMIDI was originally conceived in December 2001 as an experiment to see if MIDI files could be played using the same samples as existing software but with much less overhead. The first versions of the CLI player in 2002 were so successful in reducing the overhead that developers from Quakeforge suggested that WildMIDI could be turned into a library. 2003 saw the first implementations of the WildMIDI library with Quakeforge being used as the test application. The 1st official release of WildMIDI was in 2004. Original development stopped in 2012 at version 0.2.3.5 but was later forked and refactored in 2013 with version 0.3.0 being released in 2014. Development has continued since, with version 0.5.0 released in 2026.

**What it does**

The WildMIDI library converts MIDI files into audio which is then passed back to the calling application for further processing or output. Instruments can come from Gravis Ultrasound patch files, SoundFont2 (SF2) files, GENMIDI (OP2) FM banks, or the built-in OPL3 FM synthesizer. The API of the library is designed so that it is easy to include WildMIDI into applications that wish to include MIDI file playback. With multiple MIDI file support you can develop applications to mix several midi files together at the same time and use a different patch set for each MIDI file.

**Library Features**

- Gravis Ultrasound patch file support
- SoundFont2 (SF2) rendering via TinySoundFont
- Built-in OPL3 FM softsynth using the Nuked OPL3 emulator, with an embedded GM voice bank — no patches or soundfont required
- GENMIDI (OP2) FM bank support, such as the bank shipped with Doom
- RIFF MIDI file support
- MIDI format 0 and 1 support
- XMI, MUS, HMP and HMI conversion to MIDI
- Cross Platform: Linux, Windows, macOS, FreeBSD, OpenBSD, NetBSD, DOS, OS/2, AmigaOS and etc.
- Thread safe
- WAV file output
- Linear and gauss re-sampling
- Final output reverb engine
- Timidity.cfg compatibility

**Player Features**

- ALSA and OSS Output (Linux/FreeBSD)
- Windows Sound System support (Windows)
- CoreAudio output (macOS)
- sndio output (OpenBSD), netbsd output (NetBSD)
- Sound Blaster and compatibles (DOS), DART (OS/2), AHI (AmigaOS)
- OpenAL (optional, cross-platform)

Version 0.5.0 is API/ABI compatible with the 0.4.x series.

**Downloads, Milestones and Issues**
*Releases:*  [https://github.com/Mindwerks/wildmidi/releases](https://github.com/Mindwerks/wildmidi/releases "WildMIDI Source Releases")
*Source Code:*  [https://github.com/Mindwerks/wildmidi](https://github.com/Mindwerks/wildmidi "WildMIDI Source")
*Milestones and Planner:*  [https://github.com/Mindwerks/wildmidi/milestones](https://github.com/Mindwerks/wildmidi/milestones "WildMIDI Milestones")
*Bug / Issue Tracker:*  [https://github.com/Mindwerks/wildmidi/issues](https://github.com/Mindwerks/wildmidi/issues "WildMIDI Issue Tracker")

Precompiled binaries are available for Windows, macOS, DOS and OS/2.

**The FAQ:**
*Is this related to Timidity or some other project?*
> No, WildMIDI was written from scratch by Chris Ison with input from the team at Quakeforge and the assistance of Eric A Welsh. It was further developed by Bret Curtis after the project was abandoned. To of our knowledge there is no shared code between the 2 projects but we may have had similar ideas and influences.

*Can I use WildMIDI in my projects?*
> Yes, providing you follow the Lesser General Public License version 3 for the library, and General Public License version 3 for the demo player.

*Who developed WildMIDI?*
> WildMIDI is a work of love but many have helped to develop concepts and ideas contained within WildMIDI. Chris Ison is the founder and sole developer for over 10 years. There where many from the Quakeforge community that assisted in working out the details of the library. Eric A Welsh developed several re-samplers to experiment with, one of which still remains in the library. There are also many people who have tested, found bugs and submitted patches.
