#!/bin/bash

FORT13=$1
FORT26=$2
FINAL13=$3

#parses the file
sed -n '/   \*/,/  \*/p' $FORT13 > $FINAL13

awk '/Stat/' $2 >> $FINAL13

# parses the body
awk '{if (!/^%/ && !/^!/) {printf("  %s    %s    %s    %s    %s    0.00    1.00 0.00\n"), $1, $6, $2, $4, $8}}' $2 >> $FINAL13
# awk '{if (!/^%/ && !/^!/) {printf("  %s    %s    %s    %s    0.0000QA    0.00    1.00 0.00\n"), $1, $6, $2, $4}}' $2 >> $FINAL13

