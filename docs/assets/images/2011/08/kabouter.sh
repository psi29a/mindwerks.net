#!/bin/bash
# launching gnome terminals based on IP range given
# only within class C (last octet)
# By Bret Curtis
#
set -e
if [ -z "$1" -o -z "$2" ]; then
  echo >&2 "kabouter - a gnome terminal based multi-ssh connector."
  echo >&2 ""
  echo >&2 "usage: kabouter [start ip address] [end ip address]"
  exit 0
fi

start=(${1//./ });
end=(${2//./ });

if [ ${#start[@]} != 4 -o ${#end[@]} != 4 ]; then
  echo >&2 "Error: those are not IP addresses."
  echo >&2 ""
  echo >&2 "usage: $O [start ip address] [end ip address]"
  exit 1
fi

cmd="gnome-terminal "

# usual range up to 255
for w in `seq ${start[0]} ${end[0]}`; do
  for x in `seq ${start[1]} ${end[1]}`; do
    for y in `seq ${start[2]} ${end[2]}`; do
      for z in `seq ${start[3]} ${end[3]}`; do
        j=" --tab -e \"ssh ampli@$w.$x.$y.$z\"";
        cmd=$cmd$j;
      done
    done
  done
done

echo $cmd
eval $cmd
