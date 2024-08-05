# syntax=docker/dockerfile:1
FROM node:22.5-alpine AS builder
# no container move-se para a pasta app
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build


# PRODUÇÃO
FROM node:22.5-alpine
WORKDIR /app
COPY --from=builder /app/next.config.js ./next.config.js
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

# CMD [ "npm", "start"]



# cria uma pasta chamada app

# RUN ["mkdir", "/app"]


# Copia todos os arquivos da pasta frontend, menos o que estão mapeados no .dockerignore
# COPY . .

# Cria o node_modules e instala as dependências
# RUN ["npm", "install", "--production"]

# Constroi a estrutura no next.js
# RUN ["npm", "run", "build"]

# USER node
# Expõem a porta 3000  
# EXPOSE 3000
