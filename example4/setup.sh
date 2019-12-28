#!/bin/sh
if [ "$script_env" == "dev" ]; then
    echo "You are running in development mode";
    sh -x ./myscript.sh $@
elif [ "$script_env" == "prod" ]; then
    exec ./myscript.sh $@
fi