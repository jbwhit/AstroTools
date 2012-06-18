#!/bin/bash

# for infile in $1
# do
  # awk '/QA/' $infile
# done
# 
for trigger in $(awk '/QA/{print $3}' $1 | tr -d [:digit:] | tr -d [:punct:] | tr '[:upper:]' '[:lower:]' | sort | uniq )
do
  grep -iv "$trigger" $1 > $1.$trigger
done

