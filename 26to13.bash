#!/bin/bash

#parses the files
echo "   *" > $2
awk '/%/' $1 | sed 's/%%//g' >> $2
echo "  *" >> $2

# parses the body
awk '{if (!/%/ && !/St/) {printf("  %s    %s    %s    %s    0.0000QA    0.00    1.00  0.0\n"), $1, $6, $2, $4}}' $1 >> $2



