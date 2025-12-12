#! /bin/bash

set -e

clear

mkdir -p .github/workflows

cp github_tmp/workflows/deploy.yaml .github/workflows/deploy.yaml

clear

echo "Done"