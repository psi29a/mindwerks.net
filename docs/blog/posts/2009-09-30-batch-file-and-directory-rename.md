---
date: 2009-09-30
categories:
  - Bash
tags:
  - Bash
  - batch rename
  - hack
  - Bret Curtis
---

# Batch file and directory rename

I needed a quick way to go through a directory and rename some files and directories to remove a specific bit from the name. By using bash's parameter expansion feature we can accomplish that in just a few lines.

`#!/bin/bash
for i in *something* ; do
echo ${i/-*}
mv $i ${i/-*}
done`

This takes all files and directories with something somewhere in their name, and strips it out.
