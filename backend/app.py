from flask import Flask, render_template, request
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

import pytz

import markdown

from src.db.Connection import Connection
from src.gpt.gpt_api import GptApi
from src.gpt.EventHandler import EventHandler
from src.persona.persona_builder import PersonaBuilder

# PARA DEBUG APAGAR
from src.gpt.model.professor import ModelProfessor
from src.gpt.model.assistente import ModelAssistente
from src.gpt.model.gpr_thread import ModelGptThread
from src.gpt.model.metrica_uso import ModelMetricaUso
from src.gpt.model.serie_ensino import ModelSerieEnsino
from src.whatsapp import WhatsApp
import os


# Definindo o fuso horário de Brasília
brasilia_tz = pytz.timezone('America/Sao_Paulo')

VERIFY_TOKEN = 'J2CQMTcPDBXuwo7fi7svBoiF'

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)
CORS(app, resources={r"/*": {"origins": "*"}})
# Content-Type

@app.route('/')
def index():
    return '<h1>Api MPES 2024.1 Hello World! I have been seen times2.</h1>'

@app.route('/debug')
def gpt_debug():
    # ROTA DE DEBUG

    return render_template("gpt.html", retorno="<h1>Rodou debug</h1>")

# TESTE DE FORMULÁRIO
@app.route('/form_teste', methods=['POST'])
def m_receber_dados():
    if request.method == 'POST':
        formulario = request.json

        print(formulario)
        print(formulario["pergunta"])

        persona = PersonaBuilder()
        persona.m_add_contexto_profissao("Professo de história do ensino fundamental do brasil da quarta série")
        persona.m_add_contexto_ambiente_or_tecnologias("receber material para realizar uma aula de 2 horas")

        gpt_api = GptApi()
        retorno = gpt_api.m_conversa(persona=persona, pergunta=f"sobre {formulario['pergunta']}")
        retorno = markdown.markdown(retorno)
        return retorno


@app.route('/gpt_assist')
def gpt_assist():
    assistent_id = "asst_RybHhABngVJoOdkFmlJLGpkW"

    msg = "que eram os espartanos."
    # event_handler = EventHandler()

    gpt_api = GptApi()
    thread = gpt_api.m_criar_thread()
    gpt_api.m_adicionar_msg_thread(thread=thread, msg=msg)

    msg = gpt_api.m_run(thread=thread, assistant_id=assistent_id)

    # event_handler.m_conversa(client=gpt_api.CLIENT, thread=thread, assistant=assistent_id)

    print(msg)

    # retorno = gpt_api.m_conversa(persona=persona, pergunta="sobre maurissio de nassau")
    # msg = markdown.markdown( msg)
    return render_template("gpt.html", retorno=msg)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route('/gpt')
def gpt_pergunta():
    persona = PersonaBuilder()
    persona.m_add_contexto_profissao("Professo de história do ensino fundamental do brasil da quarta série")
    persona.m_add_contexto_ambiente_or_tecnologias("receber material para realizar uma aula de 2 horas")

    gpt_api = GptApi()
    retorno = gpt_api.m_conversa(persona=persona, pergunta="sobre maurissio de nassau")
    retorno = markdown.markdown(retorno)
    return render_template("gpt.html", retorno=retorno)


@app.route('/teste_conn')
def teste_criar_tb():
    query = "SELECT * FROM mpes.tb_teste;"

    connection = Connection()
    engine = connection.create_conexao_bd_postgresql()
    '''Deve se Implementado, nesta Versão!'''
    df = pd.read_sql(query, engine)
    print(df)

    return render_template('hello.html',  person= df.to_json())

@app.route('/api/webhook', methods=['GET', 'POST'])
def webhook():
    # Resposta para validação de domínio feita pela Meta ao add um novo webhook
    if request.method == "GET":
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Validação falhou'

    if request.method == 'POST':
        whatsapp = WhatsApp(
            mensagem_recebida=request.json
        )
        persona = PersonaBuilder()
        persona.m_add_contexto_profissao("Professor de história do ensino fundamental do brasil da quarta série")
        persona.m_add_contexto_ambiente_or_tecnologias("receber material para realizar uma aula de 2 horas")
        gpt_api = GptApi()
        retorno = gpt_api.m_conversa(persona=persona, pergunta=f"sobre {whatsapp.texto_da_mensagem_recebida()}")
        whatsapp.marcar_como_lida()
        whatsapp.responder_mensagem(retorno)

        return 'ok', 200




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug= "--debug")