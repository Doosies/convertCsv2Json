#!/bin/bash

if [ $# -eq 2 ];then
    python3 ~/Git/python/convert/main.py $1 $2
else 
    echo "Wrong input : This command only takes two arguments."
    echo " Please Re-enter this format"
    echo " 'main.py /csv path /path/' "
    echo " ex) main.py ~/py/csv/trans.csv ~/py/json/\n"
fi


        