#!/bin/bash
# Usage: ./alexa_topdomain_crawler.sh $COUNTRY_CODE

URL=""
index=0

for index in $(seq 0 19)
do
  URL="http://www.alexa.com/topsites/countries;"$index"/"$1
  curl $URL -o $1"/alexa_"$index".html" --create-dirs 
done

