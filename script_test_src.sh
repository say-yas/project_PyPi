
#!/bin/bash
# This script will run all the python files in the src and PIapprox directory

curr_dir=$(pwd)
echo "current directory:" $curr_dir

for f in $curr_dir"/src/"*.py; do
    if [[ $f != *"/__init__.py" ]]; then
        echo $f
        filename=$(basename "$f")
        name="${filename%.*}"
        echo $name
        python -m "src.""$name"
    fi
done



for f in $curr_dir"/test/test_unittest"*.py; do
    if [[ $f != *"/__init__.py" ]]; then
        echo $f
        filename=$(basename "$f")
        name="${filename%.*}"
        echo $name
        python -m "test.""$name"
    fi
done

