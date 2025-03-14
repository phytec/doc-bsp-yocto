"""
fix_redirects.py

This script processes the output from a link check and identifies any URL
redirects. It replaces outdated URLs with their new locations based on
permanent redirects.

Usage:
    python3 fix_redirects.py linkcheck_output.txt source_dir

To generate the linkcheck output file:
    tox -e linkcheck > linkcheck_output.txt
"""

import re
from pathlib import Path
import argparse


def get_redirects(linkcheck_output):
    redirects = {}
    redirect_pattern = re.compile(r'redirect\s+(http\S+)\s+-\s+permanently\s+to\s+(http\S+)')
    for line in linkcheck_output:
        match = redirect_pattern.search(line)
        if match:
            old_url = match.group(1)
            new_url = match.group(2)
            redirects[old_url] = new_url
    return redirects


def update_links_in_file(file_path, redirects):
    with open(file_path, 'r') as file:
        content = file.read()

    for old_url, new_url in redirects.items():
        # Skip URLs ending with ".git"
        if not old_url.endswith('.git') and old_url in content:
            content = content.replace(old_url, new_url)

    with open(file_path, 'w') as file:
        file.write(content)


def update_all_links(source_dir, redirects):
    for file_path in Path(source_dir).rglob('*.rst'):
        update_links_in_file(file_path, redirects)


def main():
    parser = argparse.ArgumentParser(description='Process linkcheck output file and update links.')
    parser.add_argument('linkcheck_output_path', help='The path to the linkcheck output file.')
    parser.add_argument('source_dir', help='The path to the source directory.')

    args = parser.parse_args()

    with open(args.linkcheck_output_path, 'r') as f:
        linkcheck_output = f.readlines()

    redirects = get_redirects(linkcheck_output)
    update_all_links(args.source_dir, redirects)

if __name__ == '__main__':
    main()

