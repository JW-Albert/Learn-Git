#! /bin/bash

set -e

clear

mkdir -p .github
mkdir -p .github/workflows

cp github_tmp/workflows/test.yaml .github/workflows/test.yaml

clear

echo "Done"