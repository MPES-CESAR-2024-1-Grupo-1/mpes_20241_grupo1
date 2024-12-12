## PROFZAP - IA Generativa para auxílio de Professores

[Site com mais informações sobre o projeto ProfZAP](https://sites.google.com/cesar.school/iadocentes/home)

## Componentes
- API Flask: API de integração entre WhatsApp e OpenAI.
- Dashboard Grafana: Métricas de uso baseada na coleta de dados das interações dos professores com a ferramenta.
- Banco de dados Postgres.
- Proxy NGinx: Ponto de entrada do sistema, redirecionando os requests para cada serviço -- backend e grafana.

### Como executar

O projeto usa [Docker Compose](https://docs.docker.com/compose/) para executar seus componentes, bastando apenas utilizar o arquivo `docker-compose.yml`.

### Configuração

Cada componente do projeto possui o seu arquivo `.env`, que é utilizado pelo docker-compose para configurar a comunicação entre os componentes, como API e Banco de dados.

- `postgres.development.env` -> Responsável por configurar o container do banco de dados (PostgreSQL)
- `backend/development.env` -> Responsável por configurar a API (Python+Flask). As configurações devem ser adicionadas para comunicação com banco de dados, e APIs da Meta e OpenAI.
    - `WHATSAPP_AUTH_TOKEN` - Token para utilizar a Meta API e receber/enviar mensagens para whatsapp.
    - `OPENAI_API_KEY` - chave de acesso para a plataforma da OpenAI.
    - `OPENAI_ASSISTANT_ID` - ID do assistente na plataforma Open AI - Deve ser criado utilizando a [plataforma](https://platform.openai.com/playground/assistants) e utilizar o conteúdo do arquivo `backend/instrucoes_assistente.txt` para passar suas instruções na plataforma. 
- O arquivo `nginx.conf` é o responsável por configurar o container do NGinx