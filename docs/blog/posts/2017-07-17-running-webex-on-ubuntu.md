---
date: 2017-07-17
categories:
  - Debian
  - Linux
  - Software
  - Ubuntu
tags:
  - CMR
  - Collaboration Meeting Room
  - debian
  - firefox
  - FreeBSD
  - IcedTea
  - java
  - libraries
  - linux
  - ubuntu
  - Webex
---

# Running Webex on Ubuntu

![Webex Logo](../../assets/images/2017/07/unnamed.png){ align=left width="200" }

Webex running on Ubuntu and other non-Windows platforms is literally a click away, in this case the CMR (Collaboration Meeting Room).

Webex is a fact of life for many people and for many Linux (BSD and other non-Windows) users, it has been a thorn in the side with people going so far as to set up virtual machines just to run Cisco’s collaboration software. While Webex is written in Java, it isn’t so simple to get running everywhere and apparently not all features are available for non-Windows users.

Most likely you are running up against the following message after logging into \*.webex.com

> Your browser,browser version, or operating system is currently unsupported

This requires the intervention of whoever is administrating the \*.webex.com account and they can modify it in the following way.

Directions for disabling CMR

1. Log into “xxxxx.webex.com/admin” using a site admin level account
2. Click “Edit user list” on the left navigation Window.
3. Search for the account you want to change
4. Click on the account and uncheck “Collaboration Meeting Room”
5. Click “Update”

Once this has happened, then you can log in and start Webex. Usually this is enough, but in case you hit the next wall which is runnig Java from a web-browser then there is always [Firefox ESR](https://www.mozilla.org/en-US/firefox/organizations/faq/) (Extended Support Release). This version will allow you to still run the Java (or IcedTea) NPAPI plugin. I usually download and extract to /opt then run a symlink over the system’s version of firefox in /usr/bin/firefox which is enough for my needs.

You can check to see if the Java plugin is installed in Firefox by going to the URL bar and typing:  
`about:plugins`  
Should you not see it, but you’re sure the plugin exists on the system you can make a symlink yourself:  
`ln -vs /usr/lib/jvm/java-8-oracle/jre/lib/amd64/libnpjp2.so ~/.mozilla/plugins/`  
or  
`ln -vs /usr/lib/jvm/java-8-openjdk-i386/jre/lib/i386/IcedTeaPlugin.so ~/.mozilla/plugins/`  
depending on your implementation, 32/64-bit or library location.

Ultimately regardless of which bit-ness of Java you use, Webex uses 32-bit libraries as well. Which ones? Here is list, not complete, of all the ones I needed to get it working:

`apt-get install libasound2:i386 libasound2-plugins:i386 libfontconfig1:i386 libfreetype6:i386 libgtk2.0-0:i386 libglib2.0-0:i386 libglib2.0-0:i386 libglib2.0-0:i386 libgtk2.0-0:i386 libgcj14-awt:i386 libpango-1.0-0:i386 libpangoft2-1.0-0:i386 libpangox-1.0-0:i386 gcj-4.8-jre-headless libpangoxft-1.0-0:i386 libpng12-0:i386 lib32stdc++6: libuuid1:i386 libx11-6:i386 libxext6:i386 libxft2:i386 libxi6:i386 libxmu6:i386 libxrender1:i386 libxt6:i386 libxtst6:i386 libxv1:i386 libcanberra-gtk-module:i386 gtk2-engines-murrine:i386`

To find which libraries you are still missing, you can go to your Webex directory and ldd through all the ‘so’ files to see what is missing.

`cd ~/.webex/  
find | grep so | xargs ldd | grep 'not found' | sort | uniq`

If the result is something like this:

> libjawt.so => not found

then you’re ready to go. Otherwise you’ll need to track down all the libraries in order to get the most out Webex.
