---
date: 2011-11-24
categories:
  - Security
tags:
  - passwords
  - passphrase
  - security
  - cracking
  - gpu
  - opencl
  - cpu
  - Bret Curtis
---

# Better password security through length

![passwords](../../assets/images/2011/11/passwords.jpg){ align=left width="200" }

As comically seen on [xkcd](http://xkcd.com/936/ "Password Strength"), a password's length is more important than its complexity. What we should take away from the comic is that short but hard to remember passwords are easiest to crack while long and easy to remember passwords are harder to crack.

Try for yourself with my online [password cracking calculator](https://mindwerks.net/online-tools/password-cracking-calculator/ "Password Cracking Calculator").

As an example, we will compare two passwords: "Tr0ub4dor&3" and "correct horse battery staple". We will assume that a brute-force machine that can theoretically do 200,000,000 guesses per second, which is more pessimistic than a machine with four [ATI HD 5970s](http://www.golubev.com/hashgpu.htm "Program to recover/crack SHA1, MD5 & MD4 hashes.") at 22,400,000 guesses per second. It would take such a machine about 242,243,228 days to guess "Tr0ub4dor&3". It would take the latter password 9.62x10^41 days to guess.
Now if law enforcement (or [Anonymous](http://en.wikipedia.org/wiki/Anonymous_(group) "Anonymous")) gets involved, you can expect some distributive computing to help increase the effectiveness of the attack. With a botnet of 100,000 computers with GPUs the first password goes to 86,515 days to crack while the later 3.436\*10^36 days to guess.

We can only expect that with existing trends that hardware and software will become more efficient. The mathematics help prove a point, that short complex passwords are more easily cracked than long passwords. A long but easily remembered password is mathematically a safer bet.

Note of warning: Best practices with passwords still apply because of other attack vectors like dictionary attacks, common word compounding and mutations of words such as 0s for Os and other such substitutions.

Observation: Choose the first sentence of a random book and memorize it, punctuation and all. You should be safe for the immediate 10 years.
