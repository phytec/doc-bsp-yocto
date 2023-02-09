#!/bin/bash

# Allow executing this script from any directory within the repo.
reporoot="$(git rev-parse --show-toplevel)"
cd $reporoot

# setup.txt dependency is not installed by tox
pip3 install -r requirements/setup.txt || exit 1

# Run checks and exit if any of them fails
scripts/check_filesize.sh || exit 1
scripts/check_filenames.sh || exit 1
tox -e py3-spellcheck || exit 1
tox -e py3-linkcheck || exit 1
tox -e py3-html || exit 1
tox -e py3-pdf || exit 1
