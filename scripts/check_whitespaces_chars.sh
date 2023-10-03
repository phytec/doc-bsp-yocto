#!/bin/bash

dir="source"

# Patterns:
# 1. Trailing spaces or tabs at the end of a line.
space_tab="[ \t]+$"
# 2. Non-breaking space (U+00A0) anywhere.
#pt_nbsp="\xC2\xA0"
nbsp="[\u00A0]"
# 3. U+2019 apostrophe anywhere.
apostrophe="[\u2019]"

# Combine patterns with OR (|) for final pattern
pattern="($space_tab|$nbsp|$apostrophe)"

# Use rg to search in .rst and .rsti files
matches=$(rg --line-number --column "$pattern" -g '*.rst' -g '*.rsti' "$dir")

# Check results
if [[ ! -z "$matches" ]]; then
    echo "$matches"
    echo "Detected undesired characters or patterns."
    exit 1
else
    echo "No undesired characters or patterns found."
    exit 0
fi
