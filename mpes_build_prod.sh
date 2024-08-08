#!/bin/bash

PATH_PROJETO=$(pwd)
echo $PATH_PROJETO

echo "[ACAO] ==> BUILD DO PROJETO"
echo "########################################################################"
echo "                        CONFIGURAÇÃO DO AMBIENTE                        "
echo "------------------------------------------------------------------------"

echo "[ACAO] ==> CRIAR A REDE DOCKER DO PROJETO"
NETWORK_NAME="network_mpes"
if ! docker network ls --format '{{.Name}}' | grep -q "$NETWORK_NAME"; then
    echo "Criando o $NETWORK_NAME"
    docker network create --driver bridge $NETWORK_NAME
else
    echo "==> A rede já existe $NETWORK_NAME"
fi


echo ""
echo ""
echo "########################################################################"
echo "                          DOCKER COMPOSE UP                             "
echo "------------------------------------------------------------------------"

docker compose up --build

echo " "
echo " "


