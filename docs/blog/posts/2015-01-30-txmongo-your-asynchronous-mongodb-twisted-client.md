---
date: 2015-01-30
categories:
  - Networking
  - Python
  - Code
tags:
  - GitHub
  - Bret Curtis
  - Amplidata
  - ssl
  - MongoDB
  - python
  - twisted
  - TxMongo
---

# TxMongo - Your Asynchronous MongoDB Twisted Client

![2000px-Twisted_Logo_(software).svg](../../assets/images/2014/12/2000px-Twisted_Logo_software.svg_.png){ align=left width="200" }

We're proud to announce the release of 0.6 of [TxMongo](https://pypi.python.org/pypi/txmongo "TxMongo"), which brings SSL support using Twisted's SSL context factory, "find with cursor" support just like PyMongo, bug fixes and updated unit tests! TxMongo is an asynchronous MongoDB client written for [Twisted](https://twistedmatrix.com "Twisted Matrix") in Python.
The biggest change is that TxMongo is now sponsored by [Amplidata](http://amplidata.com/ "Amplidata"). Through them we were able to get development, bug fixes and Twisted first-party sponsorship online. We now have continuous integration (CI) with a wide matrix of support for py26/py27/pypy using Twisted 12.1 to 14.0 (and trunk). We also now have 78% code coverage with unit testing as a result!
This is also the very last release in the 0.x series before we step over to the "year.release" model used by Twisted, it will also eventually find its way into Twisted's github organization as a first class library.
You can download TxMongo 0.6.0 and other releases here: [TxMongo Github Releases](https://github.com/psi29a/txmongo/releases "TxMongo Github Releases")

***What to expect***
We have a list of priorities:

- Switch documentation over to sphinx for readthedocs.org supports.
- Get TxMongo moved over to Twisted's org, with Travis-CI and Coveralls.
- Get coverage to at least 80%.
- Research functions found in PyMongo that are missing TxMongo.
- Contact various TxMongo forks and gather up bugs/issues/patches from various distros.

***Backstory***
In evaluating various options for using MongoDB with Twisted, there where two options:

1. PyMongo
2. TxMongo

The first option, supported by MongoDB themselves, is up to date in form of features but is synchronous and blocking. To get around this behaviour, you'll need to defer it thread. The second option is TxMongo that lacks a lot of the features of PyMongo, but is made for Twisted. Amplidata's only concern was the lack of SSL support in TxMongo, but all the main features that we needed are there. Thankfully the original author Alexandre Fiori, who is now in maintenance mode, accepted our patch.
We talked a bit about the future of TxMongo and as it turns out, he is no longer developing TxMongo but he would love to give it to the community to see it furthered developed and maintained since he no longer has the time. We included Glyph of Twisted into the conversation to see about a new home, with the driving development work coming from Amplidata.
The rest, is how they say, history.
***Example code using TxMongo and SSL***
*First we startup mongodb:*

```
#!/bin/bash
# create the path
mkdir -p /tmp/mongodb
# start mongodb process
mongod --dbpath /tmp/mongodb --sslMode requireSSL --sslPEMKeyFile mongodb.pem
```

*Second we run this code:*

```
```
from OpenSSL import SSL
from txmongo.connection import ConnectionPool
from twisted.internet import defer, reactor, ssl

class ServerTLSContext(ssl.DefaultOpenSSLContextFactory):
    def __init__(self, *args, **kw):
        kw['sslmethod'] = SSL.TLSv1_METHOD
        ssl.DefaultOpenSSLContextFactory.__init__(self, *args, **kw)

@defer.inlineCallbacks
def example():
    tls_ctx = ServerTLSContext(privateKeyFileName='./mongodb.key', certificateFileName='./mongodb.crt')
    mongodb_uri = "mongodb://localhost:27017"

    mongo = yield ConnectionPool(mongodb_uri, ssl_context_factory=tls_ctx)

    foo = mongo.foo  # `foo` database
    test = foo.test  # `test` collection

    # fetch some documents
    docs = yield test.find(limit=10)
    for doc in docs:
        print doc

if __name__ == '__main__':
    example().addCallback(lambda ign: reactor.stop())
    reactor.run()
```
```
