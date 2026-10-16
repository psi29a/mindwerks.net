---
date: 2026-10-16
categories:
  - C/C++
  - Linux
  - Software
tags:
  - Diablo II
  - D2Decomp
  - open source
  - reverse engineering
  - Linux
  - Bret Curtis
---

# Playing Diablo II natively on Linux

![Rogue Encampment running in D2Decomp](../../assets/images/2026/10/d2decomp-act1-rogue-encampment.png){ align=left width="200" }

I want to play Diablo II with my daughter on Linux, without Wine or an emulation layer. That is why I started [D2Decomp](../../projects/d2decomp.md "D2Decomp"): a from-scratch reimplementation of the Diablo II: Lord of Destruction game engine.

It is still unfinished, but Acts I, II and III play through, with all eighteen quests. That takes you from the Rogue Encampment to Lut Gholein and the Kurast Docks, then on to Mephisto's Durance of Hate. The maps for all 101 levels match the original. Act IV is not built yet.

The interesting part is checking that the engine does what the original does, rather than just making something that looks close. I use Ghidra to understand the original game and Unicorn to run its functions, then compare that behavior with the new C++ code. The project does not include game files; it reads them from a copy you own.

There are a few details I didn't expect to get this far: single player runs as a one-player client/server, like the original, and d2d can join an original game's TCP/IP host. Party play, trade, portals, waypoints, chat, quests and travel are implemented for Acts I and II, though live checks are still pending.

I have also been working on the less visible parts of keeping a project like this moving. The current development branch has opt-in crash reporting, off by default. When enabled, it can send a crash dump, hardware and OS details, GPU model and the last game frame if the game crashes. Crash-frame capture runs asynchronously, so it does not hold up the game while the frame is prepared. The launcher explains what may be sent, including that a report can contain sensitive data from game memory.

Here is the Rogue Encampment in Act I:

![Rogue Encampment](../../assets/images/2026/10/d2decomp-act1-rogue-encampment.png){ width="600" }

And scenes from Acts II and III:

![Tal Rasha's Tomb in Act II](../../assets/images/2026/10/d2decomp-act2-tal-rasha-tomb.png){ width="600" }

![Flayer Jungle in Act III](../../assets/images/2026/10/d2decomp-act3-flayer-jungle.png){ width="600" }

The [D2Decomp project page](../../projects/d2decomp.md) has more about the current state, and the [source and roadmap](https://github.com/psi29a/d2decomped) are on GitHub. Acts IV and V, hosting multiplayer games and a dedicated server are still ahead of us.
