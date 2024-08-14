#!/bin/bash

#

# Função para verificar se uma mensagem de commit foi fornecida
check_commit_message() {
    if [ -z "$2" ]; then
        echo "Uso: ./commit.sh <ação> \"mensagem de commit\""
        exit 1
    fi
}


# Função para fazer o commit
commit_changes() {
    echo " "
    echo "####################################################################"
    echo "                   GIT COMMIT NO REPOSITORIO LOCAL"
    echo "####################################################################"

    local commit_message="$1"
    git commit -m "$commit_message"
    echo "==> Commit realizado com a mensagem: $commit_message"
}

# Função para empurrar mudanças para o repositório remoto
push_changes() {
    echo " "
    echo "####################################################################"
    echo "                   GIT PUSH PARA REPOSITORIO REMOTO"
    echo "####################################################################"

    git push
    echo "==> Mudanças empurradas para o repositório remoto."
}

# Função para Log dos commits
status_commits(){
    echo " "
    echo "####################################################################"
    echo "                      GIT STATUS DO REPOSITORIO"
    echo "####################################################################"
    git status
}


log_padrao(){
    echo " "
    echo "####################################################################"
    echo "                           GIT LOG ONELINE"
    echo "####################################################################"
    echo ""

    git log  --oneline
}


# Função para Log dos commits
log_personalizado(){
    echo " "
    echo "####################################################################"
    echo "                     GIT LOG ONELINE PERSONALIZADO "
    echo "####################################################################"
    echo "DIGITE O NÚMERO DE LINHAS, OU SÓ ENTER PARA TODAS: /n no final só é apertar q"
    read qtd
    
    if [[ "$qtd" =~ ^[0-9]+$ ]]; then
        git log -n $qtd --pretty=format:"%h | ( %ar %ad ) | %an | %s" --date=format:"%d-%m-%Y %H:%M:%S"        
    else
        git log --pretty=format:"%h | ( %ar %ad ) | %an | %s" --date=format:"%d-%m-%Y %H:%M:%S"
    fi
}


# Função para adicionar arquivos ao staging
stage_files() {
    echo " "
    echo "####################################################################"
    echo "                         GIT ADD STAGING AREA"
    echo "####################################################################"
    
    git add .  
    git status

}


# Função que retorna as mudanças feitas no repositorio remoto
pull_repositorio() {
    echo " "
    echo "####################################################################"
    echo "                         GIT PULL DO REPOSITORIO REMOTO"
    echo "####################################################################"
    
    git pull  
}

merge_repositorio(){
    echo " "
    echo "####################################################################"
    echo "                         GIT MERGE"
    echo "####################################################################"
    
    branch_trabalho=$(git rev-parse --abbrev-ref HEAD)

    git checkout main
    git pull origin main

    git checkout $branch_trabalho
    git pull origin main
    git checkout main
    git merge $branch_trabalho
    git commit

}



# Função principal que orquestra as outras funções
main() {
    

    while true; do
        echo " "
        echo "####################################################################"
        echo "                            CMD GIT                         ver1.2.0"
        echo "####################################################################"
        echo " "
        echo "ESCOLHA UMA DAS AÇÕES ABAIXO: "

        echo " "
        echo "+-------------------------------------+--------------------------------------------+ "
        echo "| OPÇÃO |            AÇÕES            |                 OBSERVAÇÃO                  |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   0   | SAIR DO SCRIPT              |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   1   | GIT STATUS                  |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   2   | GIT LOG ONELINE             |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|  22   | GIT LOG ONELINE PERSONALIZ. |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   3   | GIT ADD STAGING             |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   4   | GIT COMMIT                  |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   5   | GIT PUSH                    |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   6   | GIT PULL                    |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   7   | GIT MERGE                   | TEM QUE ESTA EM UMA BRANCHE QUE NÃO A MAIN. |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|   9   | ADD -> COMMIT -> LOG        |                                             |"
        echo "|-------|-----------------------------|---------------------------------------------|"
        echo "|  10   | ADD -> COMMIT -> PUSH       |                                             |"
        echo "+-------------------------------------+---------------------------------------------+"
        echo ""
        read -p "DIGITE O NÚMERO DA AÇAO DESEJADA: " action

        case $action in
            1) status_commits 
            ;;
            
            2) log_padrao
            ;;
            22) log_personalizado
            ;;
            
            3) stage_files 
            ;;
            4) 
                read -p "Digite a mensagem de commit: " commit_message
                commit_changes "$commit_message"
            ;;
            5) push_changes
            ;;
            6) pull_repositorio
            ;;
            7) merge_repositorio
            ;;
            9)
                read -p "Digite a mensagem de commit: " commit_message
                stage_files
                commit_changes "$commit_message"
                log_commits       
            ;;
            10)
                read -p "Digite a mensagem de commit: " commit_message
                stage_files
                commit_changes "$commit_message"
                push_changes
                log_commits
            ;;
            0)
                echo "==> SAINDO"
                exit 0
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
