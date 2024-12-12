#!/bin/bash

# This script cleans up .po files by removing lines starting with '#:'. This is
# required to avoid creating large diffs when small details change in the
# source code.

DIRECTORY="source/locale/zh_CN/LC_MESSAGES"

# Check if the directory exists
if [ ! -d "$DIRECTORY" ]; then
  echo "Directory not found: $DIRECTORY"
  exit 1
fi

# Process each .po file in the directory
for po_file in "$DIRECTORY"/*.po; do
  # Check if there are any .po files
  if [ ! -e "$po_file" ]; then
    echo "No .po files found in the directory."
    break
  fi

  # Remove lines starting with '#:'
  sed -i '/^#:/d' "$po_file"
  echo "Processed $po_file"
done
