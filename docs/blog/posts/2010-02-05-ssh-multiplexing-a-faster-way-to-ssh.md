---
date: 2010-02-05
categories:
  - Linux
  - Software
tags:
  - ssh
  - multiplexing
  - opensource
  - Bret Curtis
---

# SSH Multiplexing: a faster way to SSH

## How it works:

By changing the way you ssh to a machine, you can reuse your initial ssh connection to save time when connecting.

*Edit your ~/.ssh/config file to have this:*

`Host *
ControlMaster auto
ControlPath ~/.ssh/sockets/%r@%h:%p`

We avoid problems of reusing the default /tmp but storing our connections in their own directory.

*Be sure to create the directory:*

`mkdir -m 700 -p ~/.ssh/sockets`

## When was it available:

The functionality has been available since OpenSSH 3.9.

## Usefulness:

I has come in handy for those hard to type passwords. Once in, a repeat ssh on another (local) terminal to the same machine will take just a few miliseconds and you have a command prompt to work with.

## Security:

One caveat is that this is on a per-user basis, so if you want to connect with a different username then you will have to initialize a new connection. This also means that anyone using your machine can then reuse your connection to log into the remote machine. This could be a security issue for you.
