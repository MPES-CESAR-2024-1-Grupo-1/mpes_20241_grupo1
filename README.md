

# Tecnologias Utilizadas
   - Frontend:
      - node : 22.5
      - Next.js : 14.2.4
      - Tailwind.css : 3.4.3
      - Nextui-org : 2.0.37
      - typescript : 5.0.4

   - Backend:
      - Flask==3.0.3
      - gunicorn==22.0.0
      - requests==2.32.3
      - pytz==2024.1
      - SQLAlchemy==2.0.31
      - python-dotenv==1.0.1
      - openai==1.37.1
      - pandas==2.2.2
      - psycopg2-binary==2.9.9
      - Markdown==3.6


   - Banco de Dados:
      - PostgreSQL : 16.3-alpine (Imagem docker)

   - Estrutura:
      - Docker


# POSTGRES
   - user: postgres
   - pass: postgres
   - db: db_mpes
   - conteiner_name: db_postgres_mpes
   - port: 5432:5432

   




proxy_reverso_mpes  | 10.0.2.2 - - 
   [07/Aug/2024:16:30:37 +0000] 
   "GET /_next/static/chunks/fd9d1056-13aa76f036058ae3.js HTTP/1.1" 
   404 555 
   "http://localhost:8091/" 
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"



proxy_reverso_mpes  | 172.18.0.1 - - [07/Aug/2024:16:41:51 +0000] "GET /api/ HTTP/1.1" 200 62 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

proxy_reverso_mpes  | 172.18.0.1 - - [07/Aug/2024:16:41:51 +0000] "GET /favicon.ico HTTP/1.1" 304 0 "http://localhost:8091/api/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"