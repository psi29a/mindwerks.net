# TxMongo

![2000px-Twisted_Logo_(software).svg](../assets/images/2014/12/2000px-Twisted_Logo_software.svg_.png){ align=left width="200" }

TxMongo is an asynchronous MongoDB driver for Python Twisted that implements the wire protocol on non-blocking sockets. The API derives from PyMongo. The project now lives under the [Twisted](https://github.com/twisted) organization on GitHub.

The current release is 26.0.0 (October 2026), which supports Python 3.8+, MongoDB 4.0 to 8.0 and PyMongo up to 4.18.

```sh
pip install txmongo
```

Currently supports:

- insert\_one/insert\_many, update\_one/update\_many, replace\_one, delete\_one/delete\_many and bulk\_write
- find, find\_one and the find\_one\_and\_\* family, with cursors you can iterate with `async for`
- aggregate, distinct, count\_documents and estimated\_document\_count
- create\_index, drop\_index, drop\_indexes, rename and drop
- client sessions and multi-document transactions
- connection pooling, replica sets, SSL/TLS and authentication
- GridFS
- per-call deadlines and timeouts

**Downloads, Documentation and Issues**
*Releases:*  [https://github.com/twisted/txmongo/releases](https://github.com/twisted/txmongo/releases "TxMongo Releases")
*PyPI:*  [https://pypi.org/project/txmongo/](https://pypi.org/project/txmongo/ "TxMongo on PyPI")
*Documentation:*  [https://txmongo.readthedocs.io](https://txmongo.readthedocs.io "TxMongo Documentation")
*Source Code:*  [https://github.com/twisted/txmongo](https://github.com/twisted/txmongo "TxMongo Source")
*Milestones and Planner:*  [https://github.com/twisted/txmongo/milestones](https://github.com/twisted/txmongo/milestones "TxMongo Milestones")
*Bug / Issue Tracker:*  [https://github.com/twisted/txmongo/issues](https://github.com/twisted/txmongo/issues "TxMongo Issue Tracker")
