#!/bin/bash
# Merges two output files together

cp $1 temp
cat $2 >> temp
grep '%%' temp > fort.13
grep -v '%%' temp | sort -n -k 2,2 >> fort.13


