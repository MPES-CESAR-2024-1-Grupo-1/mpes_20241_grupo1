#!/bin/bash

PATH_PROJETO=$(pwd)
echo $PATH_PROJETO
NETWORK_NAME="network_mpes"


montar_rede_docker(){
    echo "[ACAO] ==> BUILD DO PROJETO"
    echo "########################################################################"
    echo "                        CONFIGURAÇÃO DO AMBIENTE                        "
    echo "------------------------------------------------------------------------"

    echo "[ACAO] ==> CRIAR A REDE DOCKER DO PROJETO"
    if ! docker network ls --format '{{.Name}}' | grep -q "$NETWORK_NAME"; then
        echo "Criando o $NETWORK_NAME"
        docker network create --driver bridge $NETWORK_NAME
    else
        echo "==> A rede já existe $NETWORK_NAME"
    fi
}


build_compose_sem_d(){

    echo ""
    echo ""
    echo "+########################################################################+"
    echo "|                       DOCKER COMPOSE UP --BUILD                        |"
    echo "+------------------------------------------------------------------------+"

    docker compose up --build

    sleep 3
    echo " "
}


build_compose_d(){
    echo ""
    echo ""
    echo "+########################################################################+"
    echo "|                       DOCKER COMPOSE UP --BUILD -D                     |"
    echo "+------------------------------------------------------------------------+"

    docker compose up --build -d
    echo " "
}


compose_down(){
    echo ""
    echo ""
    echo "+########################################################################+"
    echo "|                       DOCKER COMPOSE DOWN                              |"
    echo "+------------------------------------------------------------------------+"

    docker compose down
    echo " "
}




# Função principal que orquestra as outras funções
main() {
    

    while true; do
        echo " "
        echo "+####################################################################+"
        echo "|                  MONTAGEN MPES2024.1 GRUPO1               ver1.2.0 |"
        echo "+####################################################################+"
        echo " "
    
        echo "ESCOLHA UMA DAS AÇÕES ABAIXO: "

        echo " "
        echo "+-------------------------------------+--------------------------------------------+ "
        echo "| OPÇÃO |            AÇÕES            |                 OBSERVAÇÃO                  |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   0   | SAIR DO SCRIPT              |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   1   | CRIAR REDE DOCKER           |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   2   | COMPOSER --BUILD            | Para Debug, terminal mostra execução.       |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   3   | COMPOSER --BUILD -D         | Para Produção, terminal livre.              |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   4   | COMPLETO DEBUG (1 -> 2)     |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   5   | COMPLETO PRODUÇÃO (1 -> 3)  |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   6   | PARAR OS SERVIÇOS           | docker compose down                         |"
        echo "+-------+-----------------------------+---------------------------------------------+"
        echo ""
        read -p "DIGITE O NÚMERO DA AÇAO DESEJADA: " action

        case $action in
            0)
                echo "==> SAINDO"
                exit 0
            ;;
            1)
                montar_rede_docker
            ;;
            
            2) 
                build_compose_sem_d
            ;;
            3) 
                build_compose_d
            ;;
            4) 
                montar_rede_docker
                build_compose_sem_d
            ;;
            5)
                montar_rede_docker
                build_compose_d
            ;;
            6)
                compose_down
            ;;
            
            *)
            echo "Ação desconhecida: $action"
            echo "Uso: ./commit.sh"
            exit 1
            ;;
        esac
        echo
        sleep 7
    done
}

# Chama a função principal
main
