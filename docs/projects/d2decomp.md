# D2Decomp: A Diablo II Engine Reimplementation

![Lut Gholein in D2Decomp](../assets/images/2026/10/d2decomp-lut-gholein.png)

**D2Decomp** is a cross-platform, open-source reimplementation of the Diablo II: Lord of Destruction game engine. It uses version 1.14d as its reference and aims to become a drop-in replacement, with a few optional features beyond the original.

I want to play Diablo II with my daughter, natively on Linux. No Wine, no emulation layer: a game engine that runs on our machines, reads the game data we own, and lets us adventure together.

## Where it is now

D2Decomp is unfinished, but Acts I to III play through: character setup, the Rogue Encampment, Lut Gholein and the Kurast Docks, every area from the Blood Moor to Mephisto's Durance of Hate, and all eighteen quests. The hellgate opens, but Act IV is not built yet.

- The 38 Act I, 35 Act II and 28 Act III levels have maps that match the original.
- Towns, vendors, hirelings and monster AI in Act II, and monster and object placement and monster AI in Act III, have been checked against the original. There are still a few details to match.
- Single player runs as a one-player client/server, like the original.
- d2d can join a game hosted by the original game over TCP/IP. Acts I and II have party, trade, portals, waypoints, chat, quests and travel implemented; live checks are pending.

## How it works

[Ghidra](https://github.com/NationalSecurityAgency/ghidra) helps us understand the original game's code. [Unicorn](https://www.unicorn-engine.org/) runs original game functions so we can check that this reimplementation behaves the same way. The engine itself is new code, written in modern C++.

The project runs on Linux, Windows and macOS. It also has an optional headless mode and a local control channel for scripted play and testing. A couple of small quality-of-life changes are available as toggles: gold is picked up when you walk over it, and roofs turn see-through around your character.

Recent work on the current development branch adds opt-in crash reporting. It is off by default. When enabled, a crash report may include a crash dump, hardware and OS details, the GPU model and the last game frame; it is sent only if the game crashes. The launcher explains what is sent and notes that the report may contain sensitive data from the game's memory.

## Screenshots

### Act I

![Rogue Encampment](../assets/images/2026/10/d2decomp-act1-rogue-encampment.png)

### Act II

![Lut Gholein](../assets/images/2026/10/d2decomp-lut-gholein.png)

![Tal Rasha's Tomb](../assets/images/2026/10/d2decomp-act2-tal-rasha-tomb.png)

### Act III

![Kurast Docks](../assets/images/2026/10/d2decomp-kurast-docks.png)

![Flayer Jungle](../assets/images/2026/10/d2decomp-act3-flayer-jungle.png)

![Travincal](../assets/images/2026/10/d2decomp-travincal.png)

![Mephisto's Durance of Hate](../assets/images/2026/10/d2decomp-durance.png)

## Bring your own game

D2Decomp does not include Diablo II or its game data. You need your own Diablo II + Lord of Destruction installation or media. The project is not affiliated with or endorsed by Blizzard Entertainment.

## Links

- [Source code and build instructions](https://github.com/psi29a/d2decomped)
- [Releases](https://github.com/psi29a/d2decomped/releases)
- [Issues](https://github.com/psi29a/d2decomped/issues)
- [Full roadmap](https://github.com/psi29a/d2decomped/blob/main/docs/PLAN.md)
