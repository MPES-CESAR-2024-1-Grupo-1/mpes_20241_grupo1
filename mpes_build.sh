#!/bin/bash


echo "########################################################################"
echo "                   CONSTRUINDO O PROJETO DOCKER                         "
echo "------------------------------------------------------------------------"

echo "##### Build No Docker Inicio! #####"
sudo chown -R dev:dev db/
docker compose up --build
echo "##### Build No Docker Fim! #####"
