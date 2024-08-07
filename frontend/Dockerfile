# syntax=docker/dockerfile:1
FROM node:22.5-alpine AS builder
# no container move-se para a pasta app
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build
# RUN npm install pm2@latest -g


# PRODUÇÃO
FROM node:22.5-alpine
WORKDIR /app
RUN npm install pm2@latest -g
COPY --from=builder /app/next.config.js ./next.config.js
COPY --from=builder /app/public ./public
COPY --from=builder /app/build ./build
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/ecosystem.config.js ./ecosystem.config.js
COPY --from=builder /app/entrypoint.sh ./entrypoint.sh
COPY --from=builder /app/.env ./.env
COPY --from=builder /app/.env.production ./.env.production

ENTRYPOINT [ "./entrypoint.sh" ]
