---
date: 2013-10-23
categories:
  - Debian
tags:
  - packages
  - debian
  - ubuntu
  - deb
  - maintainer
  - developer
  - git
  - git-buildpackage
  - gbp
  - salsa
  - Bret Curtis
---

# Debian Package Maintenance

![debian](../../assets/images/2013/10/debian.png){ align=left width="128" }

!!! note "Updated 2026-08-18"

    Debian's infrastructure has moved on since this was written. Alioth and
    git.debian.org were retired in 2018 and replaced by
    [Salsa](https://salsa.debian.org/ "Salsa"), Debian's GitLab instance, and the
    old `git-*` wrappers are now subcommands of `gbp`. The commands and URLs
    below have been updated to match.

I've been there before with [Gentoo](http://en.wikipedia.org/wiki/Gentoo_Linux "Gentoo"), as a developer, but times and situations have changed. Over the years I've been deeply involved with [Ubuntu](http://en.wikipedia.org/wiki/Ubuntu_(operating_system) "Ubuntu") for my work and at its heart, [Debian](http://en.wikipedia.org/wiki/Debian "Debian"). I've become a Debian Developer to help get closer to the development process, package management and maintenance to do my share of the heavy lifting.
The first thing I did was sign up at [Salsa](https://salsa.debian.org/ "Salsa"), the GitLab instance Debian uses for collaboration. Create an account and request guest access; you can then be added to the relevant packaging team. At this point, it is also a good idea join a [Debian mailing list](https://www.debian.org/MailingLists/subscribe "Debian Mailing List") and/or join IRC at irc.oftc.net and have a nice chat with the folks in #debian or their various sub-channels where you would like to help. It is important to have a sponsor/mentor that can help you out if you a problem. You will need them when getting accepted into the Debian community in order to start working.
If you want to help but don't know where to begin, have a look at the "[Work-Needing and Prospective Packages](https://www.debian.org/devel/wnpp/ "Work-Needing and Prospective Packages")" page. There are a few packages up for adoption, orphaned and others looking for someone to take over. Go to the appropriate group and ask about supporting your package of choice.
I am currently interested in introducing a new bit of software into Debian. If accepted, it will eventually show up in Ubuntu which is an added bonus. Once your Salsa account is set up, upload your public key (SSH access) in your account page and you should now have ssh/git access to salsa.debian.org, which gets you on your way.
Once signed in, set your .gitconfig with your name and email address:

```
[user]
	name = Bret Curtis
	email = bret@your.box
```

From there, we should create your new git repository. On Salsa this is done through the web interface of the team you belong to, or with `gbp create-remote-repo` once you have a local repository:

```
gbp create-remote-repo --remote-url-pattern='git@salsa.debian.org:fonts-team/%(pkg)s.git'
```

We can no do the rest on our local machine. We create our build environment and pull in our newly created git repo then push into that our first release.

```
sudo apt install debian-archive-keyring git-buildpackage pbuilder

# on Ubuntu
git-pbuilder create --distribution sid --mirror http://deb.debian.org/debian/ --debootstrapopts "--keyring=/usr/share/keyrings/debian-archive-keyring.gpg"
# on Debian
git-pbuilder create
```

Some extra commands that help to update the environment to the latest packages or add custom packages similar to having your own chroot envrionment.

```
git-pbuilder update
git-pbuilder login --save-after-login
```

From here on, we are pulling in our git repo, which should be empty. We do a `gbp import-orig` with a release of the project. This isn't the full repo history, just the release. We'll be asked questions about the import to validate the version number. This will create master and upstream branches. Each new release goes into the upstream branch with a tag. In master we will keep our /debian directory which should contain our control files.

```
git clone git@salsa.debian.org:fonts-team/fonts-ebgaramond.git fonts-ebgaramond
gbp import-orig --pristine-tar ../v0.015.tar.gz
git commit -a -m 'Setting up the first release.'
git push --all
```

Once you have a working /debian control files in place, let's try to get it to build and produce Debian packages. We run lintian afterwards to try to catch any errors in our control files.

```
export DEB_BUILD_OPTIONS="parallel=8" # or how many cores you wish to use
gbp buildpackage --git-ignore-new --git-pbuilder
lintian --pedantic -I
```

From here on, talk to your mentor and when you think you are ready, it is then time to "Intent to Package" (ITP) and file a bug report. Make sure you can send email first with:

```
mail -s Testing_1 bret@your.box < /dev/null
```

Should you get this back in your email, then are good to go! Use reportbug and follow through with the instructions with your ITP.

```
#On Ubuntu
reportbug --email bret@your.box -B debian wnpp

#On Debian
reportbug --email bret@your.box wnpp
```

This will get you on your way to maintaining your own package. This will file a bug and put it on the mailing list so that the appropriate people see this. Prepare for push-back and questions, this is normal. They will give advice to make sure your package is ready to be added to Debian. Good luck!
**Update: 20141024 -** When there is a new release, here are the additional steps. First clone the repo if you don't already done so, then setup your branches.

```
git clone git@salsa.debian.org:fonts-team/fonts-ebgaramond.git fonts-ebgaramond
cd fonts-ebgaramond
git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/debian
  remotes/origin/master
  remotes/origin/upstream
git checkout -t origin/debian
git checkout -t origin/upstream
git branch -a
  debian
  master
* upstream
  remotes/origin/HEAD -> origin/master
  remotes/origin/debian
  remotes/origin/master
  remotes/origin/upstream
git checkout master
gbp import-orig --pristine-tar ../v0.015d.tar.gz
```

Here you follow prompts, then when finished, give it a spin with building. Be sure to update your changelog and any version related issues.

---

*Last updated 18 August 2026: refreshed for Salsa, which replaced Alioth and
git.debian.org in 2018, and for the `gbp` subcommands that superseded the old
`git-import-orig` and `git-buildpackage` wrappers. The original post dates from
23 October 2013, with a follow-up on 24 October 2014.*
