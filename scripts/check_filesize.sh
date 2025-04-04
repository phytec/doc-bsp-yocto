#!/bin/bash
# Find files that are larger than the maximum size.

MAX_SIZE=300k
DIR=source

# Allow *.po files to be larger than the maximum size.
large_files=$(find $DIR -type f ! -name "*.po" -size +"$MAX_SIZE" -exec du -h {} \;)

if [ -n "$large_files" ]; then
  echo -e "Error: Large files were found: \n$large_files"
  exit 1
fi
