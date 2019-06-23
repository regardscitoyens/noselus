#!/bin/bash
set -eu

cd $(dirname $0)
echo $(pwd)
mkdir -p ../../../data/raw
cd ../../../data


gather_one_file () {
  fname=$1	

  echo "Treating the file : $fname" 

  cd raw

  wget https://github.com/regardscitoyens/rne-history/raw/master/${fname} 

  cd ..

  #Convert to utf8
  iconv -f ISO-8859-15 -t UTF-8 raw/$fname > $fname

  #Remove first line // Title
  sed -i '1d' $fname

  echo "$fname has been treated"
}

#gather_one_file "8-rne-deputes.txt"
files=("1-rne-cm.txt" "2-rne-epci.txt" "3-rne-cd.txt" "4-rne-cr.txt" \
      "5-rne-cac.txt" "6-rne-rpe.txt" "7-rne-senateurs.txt" \ 
      "8-rne-deputes.txt" "9-rne-maires.txt")


for f in "${files[@]}" 
do
  gather_one_file $f
done


