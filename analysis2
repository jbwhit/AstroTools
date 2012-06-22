#!/bin/bash


awk '/Stat/{print $4, FILENAME}' best.13

for infile in $(ls *.13.26)
do 
  awk '/Stat/{print $4, FILENAME}' $infile
done

