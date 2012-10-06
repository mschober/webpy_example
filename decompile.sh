#!/bin/bash

for f in `findname pyc`
do
    echo "deleting $f"
    rm $f
done
