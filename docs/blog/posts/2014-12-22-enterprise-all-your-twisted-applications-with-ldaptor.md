---
date: 2014-12-22
categories:
  - Windows
  - Linux
  - Python
  - Code
tags:
  - psi29a
  - Bret Curtis
  - ldaptor
  - openldap
  - ldap
  - twisted
  - python
---

# Enterprise all your Twisted applications with Ldaptor

![2000px-Twisted_Logo_(software).svg](../../assets/images/2014/12/2000px-Twisted_Logo_software.svg_.png){ align=left width="200" }

We're proud to announce the release of 14.0.0 of [Ldaptor](https://github.com/twisted/ldaptor "Ldaptor"), now a first party [Twisted](https://twistedmatrix.com "Twisted Matrix") project! Ldaptor is an asynchronous [LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol "LDAP") (Lightweight Directory Access Protocol) client and server implementation written for Twisted in Python.
The biggest change is that Ldaptor is now sponsored by [Amplidata](http://amplidata.com/ "Amplidata"). Through them we were able to get development, bug fixes and Twisted first-party sponsorship back online. We now have continuous integration (CI) with a wide matrix of support for py26/py27/pypy using Twisted 12.1 to 14.0 (and trunk). We also have about 75% code coverage with unit testing!
You can download 14.0.0 and other releases here: [Ldaptor Github Releases](https://github.com/psi29a/ldaptor/releases "Ldaptor Github Releases")
For a full review of what has changed, feel free to take a look at our live documentation over at ReadTheDocs: [Ldaptor Documentation](http://ldaptor.readthedocs.org/en/latest/ "Ldaptor Documentation") and the [Changelog](http://ldaptor.readthedocs.org/en/latest/NEWS.html "Ldaptor Changelog") itself.
***Backstory***
That is quite a jump from the last official release of 0.0.43 back in 2012 and from all the unofficial forks that have popped up to fill the void in between. Here is a bit of back story on how we got to where we are now.
It was originally written and carried by Tommi Virtanen until 2012, since then Ldaptor was forked many ways to solve various problems and each distro of Linux and BSD had their own patches building up dust. In the spring of 2014, an internal project at Amplidata required an OpenLDAP client for their Twisted services and the only one that offered the most promise was Ldaptor.
We got in touch with Tommi (tv42) and Glyph of Twisted to work out an arrangement where Amplidata would sponsor continued work on Twisted, Tommi would re-license Ldaptor under the [MIT Expat License](https://en.wikipedia.org/wiki/MIT_License "MIT License") and it would be hosted as a first party library with Twisted.
Since then we've consolidated the bug-fixes of other forks and distributions, improved the unit tests, cleaned up the code-base and managed to recover the PyPI Ldaptor entry. Once Travis was all green, we made our first release 14.0 (on Halloween) and are now seeing development picking up with pull requests for more tests and features!
***Usage and Example***
This particular example also includes how to connect to OpenLDAP with StartTLS. This particular feature is critical to Amplidata and there isn't any Ldaptor information about it. Now there is!

```
```
from OpenSSL import SSL
from twisted.internet import reactor, defer, ssl
from ldaptor.protocols.ldap import ldapclient, ldapsyntax, ldapconnector

class ServerTLSContext(ssl.DefaultOpenSSLContextFactory):
    def __init__(self, *args, **kw):
        kw['sslmethod'] = SSL.TLSv1_METHOD
        ssl.DefaultOpenSSLContextFactory.__init__(self, *args, **kw)

@defer.inlineCallbacks
def example():
    serverip = '192.168.128.21'
    basedn = 'dc=example,dc=com'
    binddn = 'bjensen'
    bindpw = 'secret'
    ssl = True
    query = '(cn=*)'
    c = ldapconnector.LDAPClientCreator(reactor, ldapclient.LDAPClient)
    overrides = {basedn: (serverip, 389)}
    client = yield c.connect(basedn, overrides=overrides)
    
    # do you want SSL/TLS, then you need to create a context for startTLS
    if ssl:
        tls_ctx = ServerTLSContext(
            privateKeyFileName='your.key',
            certificateFileName='your.crt'
        )
        yield client.startTLS(tls_ctx)

    yield client.bind(binddn, bindpw)
    o = ldapsyntax.LDAPEntry(client, basedn)
    results = yield o.search(filterText=query)
    for entry in results:
        print entry

if __name__ == '__main__':
    df = example()
    df.addErrback(lambda err: err.printTraceback())
    df.addCallback(lambda _: reactor.stop())
    reactor.run()
```
```

The above should work as-is, but you'll need to change the IPs, basedn, binddn, certs and keys. If you don't need SSL/TLS, then just ssl to False and you should be ready to go!
