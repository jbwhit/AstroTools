#!/bin/bash

awk '/MgII /{print $3, $0}' fort.13 | sort | cut -d' ' -f 2-35 | awk '{print $0, NR}'

