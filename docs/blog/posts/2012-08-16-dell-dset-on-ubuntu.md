---
date: 2012-08-16
categories:
  - Bash
  - Servers
  - Ubuntu
  - Software
tags:
  - dell
  - DSET
  - OMSA
  - 10.04
  - 12.04
  - ubuntu
  - linux
  - Bret Curtis
---

# Dell DSET on Ubuntu 10.04 and 12.04

![UbuntuOnDell](../../assets/images/2012/08/UbuntuOnDell.jpeg){ align=left width="200" }

Dell System E-Support Tool (DSET) is an informative tool used by Dell's support engineers to help diagnose problems for their clients. It is almost a requirement now and Dell usually refuses to continue support without a DSET report.

The problem is that DSET is only supported on Redhat and SuSE Linux and there isn't any information on how to get it running in Ubuntu. I've assembled a rough guide on how to get DSET up and running on Ubuntu 10.04 and 12.04 and it is tested against a Dell R610 and R620.
**First** we need to install Dell's OpenManage Server Administrator (OMSA) which is one piece from Dell that does support Ubuntu.
<http://linux.dell.com/repo/community/deb/latest/>

You can cut and paste the following:
`echo 'deb http://linux.dell.com/repo/community/deb/latest /' | sudo tee -a /etc/apt/sources.list.d/linux.dell.com.sources.list
gpg --keyserver pool.sks-keyservers.net --recv-key 1285491434D8786F
gpg -a --export 1285491434D8786F | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y srvadmin-all sblim-cmpi-base rpm alien
sudo ln -sf /usr/bin/rpm /bin/rpm`

The above will add Dell's repository to your apt sources and grab everything necessary to install the OMSA. It does include a java/tomcat webserver for a web GUI interface, but that is not enabled by default and not necessary for our DSET. You'll need to logout and log back in again to reset your path variables.

> root@dmachine:~# /opt/dell/srvadmin/sbin/srvadmin-services.sh start
> Starting Systems Management Device Drivers:
> Starting dell\_rbu: \*
> Starting ipmi driver: \* Already started
> Starting Systems Management Data Engine:
> Starting dsm\_sa\_datamgrd: \*
> Starting dsm\_sa\_eventmgrd: \*
> Starting dsm\_sa\_snmpd: \*
> Starting DSM SA Connection Service: \*

**Secondly**, if you are using an 'OEM Ready' Dell server then OMSA dataeng (Systems Management Data Engine) might complain with "Failed to start because system is not supported". There isn't any 'official' support for OMSA on these systems but you can contact Dell's OEM wing for custom solutions here: <http://content.dell.com/us/en/enterprise/d/oem/oem-engineering-services.aspx>

To get OMSA working on an OEM system, we need to modify this file: /opt/dell/srvadmin/sbin/CheckSystemType which calls the file: /usr/sbin/smbios-sys-info-lite which does not return back the expected value. I've modified it to key off the 'Is Dell' flag which is 1 (True). The patch can be found here: [checksystem.patch](../../assets/images/2012/08/checksystem.patch)
`patch -p0 < checksystem.patch`
Once the patch is applied, Systems Management Data Engine should start without problems.

**Thirdly** you need to download the 32 or 64 bit Linux version of DSET. You then need to edit the bin file to not run the install.sh file and to also not delete /tmp/dell\_advdiags when it is finished running. You'll need the rpm files that it extracts to install DSET on Ubuntu.

Example from dell-dset-3.2.0.141\_x64\_A01.bin: ( the # comments out the none necessary bits )
> #source install.sh

cd $CDIR
#rm -rf $TMPDIR

The only ones that we need are these:
> dell-dset-collector-3.2.0.141-1.x86\_64.rpm
> dell-dset-common-3.2.0.141-1.x86\_64.rpm
> dell-dset-provider-3.2.0.141-1.x86\_64.rpm

DSET binaries can be found here: [http://support.dell.com/dset/](http://support.dell.com/dset/ "http://support.dell.com/dset/")

**Fourthly** you'll need to verify that /bin/sh points to bash instead of dash because Dell's scripts rely on bash's functionality.
`sudo su -
ln -sf /bin/bash /bin/sh
sh dell-dset*.bin
mv /tmp/dell_advdiags ~
cd ~/dell_advdiags/rpms
alien --scripts dell-dset*.rpm
dpkg -i --force all *.deb
dellsysteminfo`

You might have to do these steps one at a time, but that is the flow of things. Alien sometimes complains about 'unknown flags' and dpkg will likely also complain about overwriting existing files. The first problem has bothered me so far, but the last is DSET overwriting existing OMSA files which as far as I can tell are the same files.

When you run dellsysteminfo, you need to give it a password. This is your typical Linux account password. You should now have something to hand over to the Dell Support people.
