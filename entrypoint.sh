#!/usr/bin/env bash
while true;
do
  echo "Downloading music"
  python3 ./run_spider.py
  echo "Downloaded music"
  sleep 21600 # 6 hours
done