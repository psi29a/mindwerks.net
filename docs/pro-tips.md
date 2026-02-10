# IT Tip Collection

This is a collection of problems and their solutions that I have come across in my work.

**Save diskspace:**
For very large disks, you can set the 5% reserve in filesystem to 1%, sometimes regaining 40GiB of diskspace from a 1TiB drive.

`tune2fs -m 1 /dev/sda1`

**SSH WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!**

`ssh-keygen -R server.example.com`

**Create a tmpfs of certain size:**

`mount -t tmpfs -o size=20m tmpfs /mnt/tmp`

**Creating a network tarpit for a port:**

`iptables -A OUTPUT -m state -p tcp --dport 23515 --state NEW,ESTABLISHED,RELATED -j DROP`

**Monitor process threads with top:** 

(Press H for showing threads)
`top -p pid`

**Setting up netconsole:**

First on receiver side:
`netconsole recieve: nc -u -l -p 6666 2>&1 | tee nc.log`
Then on sender side:
`modprobe netconsole netconsole=@/[],@/
modprobe netconsole netconsole=@/,@10.100.150.202/00:30:48:99:99:16`

**partition schema copy:** 

`sfdisk -d /dev/sda > sda; sfdisk /dev/sdb < sda;`

**uuid of device:**

`blkid`

**uuid of software raid device through mdadm:**

`mdadm --detail --scan`

**mdadm re-assembly:** 

`mdadm --assemble --scan --force`

**Quickly create directories:** 

`for (( i=1; i<13; i++ )); do mkdir -p /dss/sd$i; done`

**I need create bad block device for testing:**

`dd if=/dev/zero of=bad_disk.img bs=1M count=$((4 * 1024))
losetup /dev/loop0 bad_disk.img
dmsetup create bad_disk << EOF
0 2097152 linear /dev/loop0 0
2097152 2097152 error
4194304 2097152 linear /dev/loop0 2097152
EOF`

This creates a file that is about 4GiB, then uses it in a loopback device with a trick to create a bad area on the "disk". This is useful for debugging VMware, Xen and Virtualbox disk handling capabilities.
