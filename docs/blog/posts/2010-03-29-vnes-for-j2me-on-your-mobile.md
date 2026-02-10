---
date: 2010-03-29
categories:
  - Linux
  - Software
  - Bash
tags:
  - nes
  - java
  - emulator
  - Bash
  - script
  - j2me
  - vnes
  - tips
  - linux
  - Bret Curtis
---

# vNES for J2ME on your mobile

If you have ever wanted to play a NES game on your mobile, then you might have heard about [vNES](http://www.vampent.com/vnesdownload.htm "vNES"). There is a J2ME version which allows it to run on most mobiles available today.
There are however a few rough edges to this application as it requires assembling the necessary files together and running a windows batch file. From a Linux point of view, I have created a replacement shell script that does a better job. It requires unix2dos, rename, and bash.

Just place this file into your vNes directory: ***makejar.sh***

```
#!/bin/bash
cd roms
#uppercase all our roms
rename 'y/a-z/A-Z/' *.nes
#remove all spaces, shorten name
rename "s/ *//g" *.NES
#rename roms to png
rename 's/\.NES$/\.png/' *.NES
#create our list of roms
package=""
for file in `dir -A` ; do
    package="${package}${file%.png}\
"
done
echo -e $package > ../package.txt
cp *.png ../package
cd ..
#make sure list is with windows line breaks
unix2dos package.txt
cp package.txt package/2.txt
cd package
#package everything up
zip -r -9 ../vnes.jar *
cd ..
```

Be sure to set: `chmod +x makejar.sh`

### General advice:

The NES rom files must be in iNES format, and also be renamed from \*.rom to \*.png and copied into "package" directory. There is a file in "package" called 2.txt which is a list of all the roms you have.
Rom names should be in capital letters, with .png at the end, not .rom nor .nes. Example: castlevania\_3.nes --> CASTLE3.png and in 2.txt add a new line with 'CASTLE3' without the '.

### Here are a list of possible problems:

##### Menu freezes when selecting one of the 3 options like 'play':

This usually means that something is not right with 2.txt, make sure this is an extra line at the end of list. Use a space if you have to and remember use Windows based EOL 'end of line' characters. It helps to use 'unix2dos' to convert your \
to ^M.

##### You get the "application is invalid" error message:

Delete the line "MIDlet-Data-Size: 1024000" in the file "package\META-INF\MANIFEST.mf", this line tells the mobile how big the java application is. Problem is some mobiles just do not agree with that size and as a result will refuse to run a slightly dodgy application. It is best just to remove the line for maximum compatibility.

##### When loading a rom you get "java.lang.NullPointerException" error message:

This is because the rom file either does not exist in the package dir, the name is spelled incorrectly in the 2.txt file, or that there are wrong line endings. Verify that the files exist as \*.png in the 'package' directory and to be safe, run unix2dos or todos on 2.txt file make sure the line endings are correct. The application expects dos ^M line endings.
