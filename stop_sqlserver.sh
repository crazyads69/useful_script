#!/bin/bash

NAME=""

read -p "Input docker name: " NAME

docker stop ${NAME}
docker rm ${NAME}
