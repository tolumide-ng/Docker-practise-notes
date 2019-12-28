#!/bin/sh
if [ $# -eq 0 ]; then
    echo "Please provide your name as an argument!"
else
    echo "Hello $1 from our Docker container!"
fi