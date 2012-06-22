#!/bin/bash
# for trigger in al; #
# for trigger in aa ae ah ar; #
for trigger in af ai aj am ac al;
do
  trigger2=$(echo $trigger | tr '[a-z]' '[A-Z]')
  echo $trigger $trigger2
  grep -v $trigger stat.13 | grep -v $trigger2 > stat.$trigger.13
done

