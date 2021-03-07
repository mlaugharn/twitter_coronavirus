#!/bin/sh

for file in /data/tweets_corona/*.zip
do 
    python3 ./src/map.py --input_path=$file &
done
