#!/bin/bash

NAME="";
PORT="";
PASSWORD="";

read -p "Input docker name: " NAME;
read -p "Input port: " PORT;
read -p "Input password: " PASSWORD;

echo $NAME;
echo $PORT;
echo $PASSWORD;

echo "Start docker: ";
docker run -e ACCEPT_EULA=Y -e MSSQL_PID='Developer' -e MSSQL_SA_PASSWORD=${PASSWORD} -e MSSQL_TCP_PORT=${PORT} -p ${PORT}:${PORT} --name ${NAME} --hostname ${NAME} --platform linux/amd64  -d mcr.microsoft.com/mssql/server:2019-latest;

