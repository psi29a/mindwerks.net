---
date: 2015-11-06
categories:
  - Python
  - Software
tags:
  - deadline
  - MongoDB
  - PyMongo
  - real-time
  - realtime
  - timeout
  - TxMongo
---

# Deadlines and Timeouts for Realtime MongoDB Access with TxMongo

![2000px-Twisted_Logo_(software).svg](../../assets/images/2014/12/2000px-Twisted_Logo_software.svg_.png){ align=left width="200" }

Murphey had an adage: “Anything that can go wrong, will go wrong.” The best we can do is attempt to anticipate any problems that might come up and keep ‘the machine’ running. From an end-user perspective that means being responsive, even with errors. If there is a network error, we want to know as soon as possible with the guarantee that state of ‘the machine’ was not effected by the error.

With the release of [TxMongo 15.3.1](https://pypi.python.org/pypi/txmongo/15.3.1) we’ve introduced a few things that are useful when creating [real-time](https://en.wikipedia.org/wiki/Real-time_computing#Near_real-time) applications.

**We now have per-call deadline and timeouts!**

***Deadline***: The latest time (in the future) by which the call should be completed. Useful when your application has a deadline to complete a task and you pass the same deadline to all MongoDB calls.

***Timeout***: How much time the call has to complete itself. Useful when each call in your application is allowed a certain amount of time to complete itself.

If these are ever exceeded, an error `TimeExceeded` is raised that you can trap. The guarantee is that when the error is raised, the call will not have modified MongoDB.

Here are two examples of how to implement these in your application:  

```
yield conn.db.coll.insert({'x': 42}, safe=True, timeout=10)
yield conn.db.coll.insert({'x': 42}, safe=True, deadline=time()+10)
```

We also have additional features that will be useful as well:

- When dealing with `connection.ConnectionPool`, `max\_delay` is now exposed which is used to set the maximum number of seconds between connection attempts. The default is set to 60.
- When dealing with `connection.ConnectionPool`, `initial\_delay` is now exposed which is used to set the initial backoff retry delay. The default is set to 1.
- NotMaster instead of AutoReconnect error will be returned when a call can be safely
- Python3 support!

If you have any feature requests or problems, you can use our [txmongo github issue tracker](https://github.com/twisted/txmongo/issues)!
