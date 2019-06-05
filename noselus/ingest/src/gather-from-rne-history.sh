#!/bin/bash
set -eu

cd $(dirname $0)
echo $(pwd)
cd ../../../data

wget https://github.com/regardscitoyens/rne-history/raw/master/1-rne-cm.txt
