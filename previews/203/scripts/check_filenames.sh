#!/bin/bash
# Check for whitespaces in filenames. Exit with error, if found.

DIR=source

files_with_whitespace=$(find $DIR -type f -name "* *" -exec du -h {} \;)

if [ -n "$files_with_whitespace" ]; then
  echo "Error: The following files have a whitespace in the name:"
  echo "$files_with_whitespace"
  exit 1
fi
