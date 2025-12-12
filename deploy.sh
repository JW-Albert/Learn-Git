#!/bin/bash

set -e

clear

./env.sh

source venv/bin/activate

./pytest.sh

echo "Done"