#!/bin/bash
# This script will run all the python files in test and PIapprox directory

curr_dir=$(pwd)
echo "current directory:" $curr_dir

for f in $curr_dir"/PIapprox/"*.py; do
    if [[ $f != *"/__init__.py" ]]; then
        echo $f
        filename=$(basename "$f")
        name="${filename%.*}"
        echo $name
        python -m "PIapprox.""$name"
    fi
done


for f in $curr_dir"/test/"*.py; do
    if [[ $f != *"/__init__.py" ]]; then
        filename=$(basename "$f")
        name="${filename%.*}"
        echo "Calling " $filename
        python -m "test.""$name"
        echo "-----------------------------"
    fi
done