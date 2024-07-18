# syntax=docker/dockerfile:1

# Use a imagem base oficial do Nginx
FROM nginx:1.27.0

# Copie o arquivo de configuração personalizado para o container
COPY proxy_reverso/nginx.conf /etc/nginx/nginx.conf

# Copie os arquivos do site para o diretório padrão do Nginx
# COPY html /usr/share/nginx/html

# Exponha a porta que o Nginx vai escutar
# EXPOSE 80

# Comando para iniciar o Nginx
# CMD ["nginx", "-g", "daemon off;"]
