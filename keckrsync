#!/bin/bash
# keckrsync.bash
# When observing at Keck, continually send the files to the supercomputer
# in the background.
# 
# Copyright Jonathan Whitmore
# Questions/comments/improvements welcome. 
# Distributed under the Boost Software License, Version 1.0.
#
# Permission is hereby granted, free of charge, to any person or organization
# obtaining a copy of the software and accompanying documentation covered by
# this license (the "Software") to use, reproduce, display, distribute,
# execute, and transmit the Software, and to prepare derivative works of the
# Software, and to permit third-parties to whom the Software is furnished to
# do so, all subject to the following:
#
# The copyright notices in the Software and this entire statement, including
# the above license grant, this restriction and the following disclaimer,
# must be included in all copies of the Software, in whole or in part, and
# all derivative works of the Software, unless such copies or derivative
# works are solely in the form of machine-executable object code generated
# by a source language processor.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
# NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
# DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
# WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 

# Setup sshkeys between the keck computer, your laptop, and the supercomputer.
# You will have to CRTL-C this command to stop it. 

# All of the following need to be modified before running.
# Supercomputer setup information
SUPERUSERNAME='username' # change
SUPERCOMPUTERURL='super.computer.location.edu' # change
SUPERCOMPUTERDEST='/nfs/cluster/qso/fill/in/this/path/correctly/' # change

# HIRES computers
KECKACCOUNT='hires' # change to observing account
KECKHOST='puamana' # 2012-06-22 rsync only on: [puamana, hamoa, mokulau]
KECKDATADIR='/h/scratch13/check/where/the/data/is/' # change

# Your laptop
LOCALINTERMEDIARY='/location/on/your/laptop/at/keck/' # change

# Sleep between commands running. 
SLEEPAMOUNT='120'

while [ 1 ]
do
  echo "Grabbing files to put on local laptop..."
  rsync -avz KECKACCOUNT@$KECKHOST:$KECKDATADIR $LOCALINTERMEDIARY
  
  echo "Sending files to supercomputer"
  rsync -avz $LOCALINTERMEDIARY $SUPERUSERNAME@$SUPERCOMPUTERURL:$SUPERCOMPUTERDEST

  echo "Going to sleep for a few seconds... "
  sleep $SLEEPAMOUNT
done