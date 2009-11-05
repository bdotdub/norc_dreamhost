#!/bin/sh

#############################################################
# Norc submodule stuff

git submodule init
git submodule update

#############################################################
# Python executable replacement

# Make a copy of the current Norc `bin` dir
cp -R norc/bin norc/bin_backup

# Replace the string
for bin in `ls norc/bin_backup/*.py`; do
  bin=`basename $bin`
  echo Replacing Python executable for $bin
  sed 's:^#!/usr/bin/python$:#!/usr/bin/python2.4:' norc/bin_backup/$bin > norc/bin/$bin
done

