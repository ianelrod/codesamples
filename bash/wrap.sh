#!/bin/bash

# env -i /challenge/$CHALLENGE_NAME --noprofile --norc
# 0<&196;exec 2<>&; /bin/bash <&196 >&196 2>&196
1>&0-
exec /challenge/$CHALLENGE_NAME 0>&1 >&1 <&1
# 0>&2-;exec 2<>&-; /bin/bash <&0 >&0 2>&0