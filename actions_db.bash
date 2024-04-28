#!/bin/bash

if [ $1 == "init" ];
  then python -m backend.scripts.create_tables
elif [ $1 == "drop" ];
  then python -m backend.scripts.drop_tables
else
  echo "init or drop is required argument!"
fi
