---
date: 2011-12-08
categories:
  - Networking
  - Linux
  - Security
tags:
  - ssh
  - secure shell
  - firewall
  - networking
  - Bret Curtis
---

# SSH as a socks proxy

![passwords](../../assets/images/2011/11/passwords.jpg){ align=left width="200" }

Recently there was a need to visit a US based website to verify some personal information. Apparently there are 'rules' about who is geographical allowed to get access to the site which means that a citizen of said country cannot access the site from outside of the US.

I will not get into the absurdity of such security mandates, instead we will go around the problem and get our information that bureaucracy tried to prevent.

The general idea is to use a proxy inside the US that will allow us to hop over the geographical firewall. I do not trust open proxies by default because of their ability to sniff traffic. I do however have access to a [secure shell](http://en.wikipedia.org/wiki/Secure_Shell) (SSH) in the US that I can use.
Using this command:
`ssh -D 8080 bcurtis@your.box`

will create a port 8080 on localhost (your computer). You can then use a web-browser like chrome from anywhere in the world and through an encrypted tunnel come out the other side on a network based in the US. You need to configure your web-browser to use a 'SOCKS Proxy' in order for this to work.

For chrome, it is easy as doing this:
`chrome --proxy-server="socks5://127.0.0.1:8080"`
or you can follow this [guide to setting up chrome with socks](http://sockslist.net/articles/google-chrome-proxy-how-to-use).

To check that it is working, go to google and ask "[What is my IP](http://www.google.be/search?q=what+is+my+ip)".

For more detailed information, here is the ssh man page:
> Specifies a local “dynamic” application-level port forwarding. This works by allocating a socket to listen to port on the local side, optionally bound to the specified bind\_address. Whenever a connection is made to this port, the connection is forwarded over the secure channel, and the application protocol is then used to determine where to connect to from the remote machine. Currently the SOCKS4 and SOCKS5 protocols are supported, and ssh will act as a SOCKS server.
