#!/bin/sh

exitcode=0

# match NBSP (\u00a0), apostrophe (\u2019)
matches=$(grep --include "*.rst*" -rnP "(\x{00a0}|\x{2019})" source)
if [ -n "$matches" ]; then
    echo "ERROR: Detected undesired characters!"
    echo "$matches"
    exitcode=1
fi

# match trailing spaces
matches=$(grep --include "*.rst*" -rnP "[[:space:]]$" source)
if [ -n "$matches" ]; then
    echo "ERROR: Detected trailing spaces!"
    echo "$matches"
    exitcode=1
fi

# match multiple empty lines
matches=$(grep --include "*.rst*" -rlzP "\n\n\n" source)
if [ -n "$matches" ]; then
    echo "ERROR: Detected redundant empty lines!"
    echo "$matches"
    exitcode=1
fi

# find missing EOL characters at end of file
matches=$(grep --include "*.rst*" -rvlzP "\x{000a}$" source)
if [ -n "$matches" ]; then
    echo "ERROR: No newline at end of file!"
    echo "$matches"
    exitcode=1
fi

exit $exitcode
