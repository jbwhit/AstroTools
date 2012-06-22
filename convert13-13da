#!/bin/bash

MAXN=$(sed -n '/\(^  \*\)/,$p' $1 | sed 1,2d | awk 'max=="" || $2 > max {max=$2} END{ print max}')

# awk '{if ($2 !='$MAXN') print $0; else gsub(/QA/,"qa")}' $1
awk '{if ($2 !='$MAXN') print $0; else print $1, $2, $3, $4, "0.0000qa  0.00 1.00 0.00"}' $1 > alpha.13

