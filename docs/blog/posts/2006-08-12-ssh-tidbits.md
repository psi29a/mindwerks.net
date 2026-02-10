---
date: 2006-08-12
categories:
  - Linux
  - Software
tags:
  - ssh
  - pki
  - linux
  - opensource
  - password
  - rsa
  - dsa
  - Bret Curtis
---

# SSH with Public Key Authentication

Okay, say you have a server, you have to ssh to this server ... say 20 times a day?
It gets irritating having to login and type your password repeatedly. Not to mention it can be insecure if anyone is sniffing the network.

So on your desktop machine you want to create some keys. This can be done with the following command:
> ssh-keygen -t rsa

At the prompts just press enter for all the defaults. This includes an empty password.

Now you should have a file in .ssh/id\_rsa.pub , this file has to go to the server. You can do this with this command
> cat .ssh/id\_rsa.pub | ssh username@servername "cat - >>.ssh/authorized\_keys"

All going well, this should exit cleanly. Test it by ssh'ing again to the server normally, if all goes well it shouldn't prompt but just drop you into your remote shell.
If this fails make sure your servers /etc/ssh/sshd\_config has the following line
> RSAAuthentication yes
> PubkeyAuthentication yes
> AuthorizedKeysFile %h/.ssh/authorized\_keys

Also, you will need specific permissions in order for this to work as well, so the follow needs to be run as the user you are logged in as.
> server$ chmod go-w ~/
> server$ chmod 700 ~/.ssh
> server$ chmod 600 ~/.ssh/authorized\_keys

Enjoy your keyless SSH access.
