#!/bin/sh

# match NBSP (\u00a0), apostrophe (\u2019) and trailing spaces
matches=$(grep -nrH --include "*.rsti" --include "*.rst" -P "(\x{00a0}|\x{2019}|[[:space:]]$)" source/)

if [[ ! -z "$matches" ]]; then
    echo "ERROR: Detected undesired characters!"
    echo "$matches"
    exit 1
fi
