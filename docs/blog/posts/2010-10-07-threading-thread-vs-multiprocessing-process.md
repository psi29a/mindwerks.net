---
date: 2010-10-07
categories:
  - Python
  - Servers
  - Ubuntu
  - Software
tags:
  - python
  - code
  - gil
  - threading
  - multiprocessor
  - smp
  - signals
  - work
  - Bret Curtis
---

# threading.Thread vs. multiprocessing.Process

# The Feather or the Anvil?

# 

First a bit of background: I was tasked with created a high level tester for my company's system. The idea is create 1 or more monkeys to pound away at the company's product for a very long time. A concurrent parallel programming project with the requirement that it needed to be compatible with 2.6.2 version of Python.

With threading, you get real posix threads (pthread) which works pretty well. They implicitly share state with the parent thread and do not use IPC or messaging. They have low latency and low overall resource footprint.

However there are drawbacks that made further development using threads a real problem. that is the use of signals. Such as threads not handling signals, working with the global interpreter lock (GIL, only one thread allowed to run at a time), and more.

This particular implementation of Python is used as a wrapper to binaries on the system, the benefit of understanding signals and passing them back to Python. The threading module simply does not like this:
> failed to set child signal, error signal only works in main thread

According to the [documentation](http://docs.python.org/release/2.5.2/lib/module-signal.html):
> Some care must be taken if both signals and threads are used in the same program. The fundamental thing to remember in using signals and threads simultaneously is: always perform signal() operations in the main thread of execution. Any thread can perform an alarm(), getsignal(), or pause(); only the main thread can set a new signal handler, and the main thread will be the only one to receive signals (this is enforced by the Python signal module, even if the underlying thread implementation supports sending signals to individual threads).

My hands are tied: I cannot upgrade Python, modify the execute() method being used nor can I trap the signal being sent to the thread by the execute().

There is one heavy handed solution and that is to use [multiprocessing](http://docs.python.org/library/multiprocessing.html). It is almost a 1 to 1 replacement for the threading module, including the same API. However it has drawbacks in comparison to threads like: large resource footprint (big heavy process), processes do not share state and must use some form of message passing such as IPC to communicate.

If you can do this:
`Thread(target=func, args=(args,)).start()`
Then it is trivial to convert to:
`Process(target=func, args=(args,)).start()`

There are benefits to the anvil approach however. Processes automatically run on multiple cores which helps make distributive systems easier, processes are safer to use as they do not share any state implicitly and they make high-throughput processing trivial. It has the additional benefit of not needing locks which means you get to side-step the GIL.

I managed to replace all instance with threading with multiprocesser and suddenly I am no longer in GIL hell nor having issues with handling signals in my child processes. The only downside is that we require more resources to run the same test and slower initial start-up due to process creation. No one ever said it was light weight.
