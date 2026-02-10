---
date: 2007-08-02
categories:
  - Debian
  - Software
tags:
  - debian
  - linux
  - apache
  - ssl
  - opensource
  - ssl-cert
  - Bret Curtis
---

# Apache2 with SSL on Debian

I found myself at a loss on how to enable ssl on apache2, it seemed so simple. Make sure ssl.conf and ssl.load where both in mods-enabled and restart apache2, and done. Not so fast, the damn thing needs a self-signed certificate and the normal scripts are no where to be found on Debian 4.0 Etch. After a bit of searching I've come across this little gem that I hope will help all of you too.
`aptitude install ssl-cert`

`/usr/sbin/make-ssl-cert /usr/share/ssl-cert/ssleay.cnf /etc/apache2/ssl/apache.pem`

This uses everything that Debian 4.0 gives you by default.
