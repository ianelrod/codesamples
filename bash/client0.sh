#!/bin/bash

exec 3<>/dev/tcp/127.0.0.1/1294;j="j";while [ -n "$j" ];do read -u 3 j;if k=$(echo "$j" | grep -oP ":\s\K.*");then echo $k | bc >&3;else echo $j;fi;done