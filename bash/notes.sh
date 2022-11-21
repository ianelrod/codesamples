#!/bin/bash

# echo "$line" | grep -oP '[\d(].*$' | bc >&196
# for i in {1..2}; do read -u 196 line && echo $line; done
# echo "$line" | grep -oP '[\d(].*$' | bc >&196
# for i in {1..2}; do read -u 196 line && echo $line; done
# echo "$line" | grep -oP '[\d(].*$' | bc >&196
# for i in {1..2}; do read -u 196 line && echo $line; done
# echo "$line" | grep -oP '[\d(].*$' | bc >&196
# for i in {1..2}; do read -u 196 line && echo $line; done
# echo "$line" | grep -oP '[\d(].*$' | bc >&196
# for i in {1..4}; do read -u 196 line && echo $line; done
#read -r line <&196; print -r - $line
# timeout 1 cat </dev/tcp/127.0.0.1/1294
# read -r -u -n $MESSAGE <&196; echo "$MESSAGE"
#read -r -u -n $MESSAGE <&196
#MESSAGE=$(dd bs=$NUM_BYTES count=$COUNT <&196 2> /dev/null)
#echo $MESSAGE
#read -r -u -n $MESSAGE <&196
#MESSAGE=$(dd bs=$NUM_BYTES count=$COUNT <&196 2> /dev/null)
#echo $MESSAGE
# /usr/bin/printf <&196 >&196 2>&196  #open fd 122.
# exec 122<>/dev/tcp/127.0.0.1/1294
# cat 122 | (read; echo "$REPLY")
# exec 3>&0
F=$(mktemp)
exec 3<> "$F"
rm -f "$F"

sed s/s/s/ <&3
{ exec < /dev/stdin; exec /challenge/$CHALLENGE_NAME; } <&3
# exec <>&122
# echo "wskafiui" > /tmp/foo
# /home/hacker/x1
# 0<&122; sed <&122 >&122 2>&122
# 0<&122; exec /challenge/$CHALLENGE_NAME <&122 >&122 2>&122
# echo $pid
# exec 0>&3
# exec 122>&-