#!/bin/bash

csplit -s $1 '%^   \*%' '/^  \*/1'
# This outputs two files: xx00, xx01
mv xx00 head.13
mv xx01 body.13

# removes the first and last line of the head.13 file
tail -n +2 head.13 | sed -e '$d' | awk '{printf("%s %2.10f%s%s %s\n"),"  >>       1.0SN      ",($3 + 0.1)/1215.6701 -1, "SZ     0.00         0.0000E+00QA    0.00    1.00 0.00 ! ", $(NF-1), $NF}' 

echo "Remember you need to have 1 of these chunks be the reference (just delete it)."