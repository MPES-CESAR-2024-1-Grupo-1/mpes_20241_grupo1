from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from werkzeug.middleware.proxy_fix import ProxyFix
from datetime import datetime
import pytz
import requests
import pandas as pd
import markdown

from src.db.Connection import Connection
from src.gpt.gpt_api import GptApi
from src.gpt.EventHandler import EventHandler
from src.persona.persona_builder import PersonaBuilder


# Definindo o fuso horário de Brasília
brasilia_tz = pytz.timezone('America/Sao_Paulo')

#https://www.mpes20241grupo1.com.br/webhook
# Seu token de acesso do WhatsApp Business API
ACCESS_TOKEN = '17ac4e001aa877dca761ca598dce4f56'
VERIFY_TOKEN = 'EducacionaAssistente'




app = Flask(__name__)


app.wsgi_app = ProxyFix(app.wsgi_app)
CORS(app, resources={r"/*": {"origins": "*"}})
# Content-Type


@app.route('/')
def index():
    return '<h1>Api MPES 2024.1 Hello World! I have been seen times2.</h1>'








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
        
        # return render_template("gpt.html", retorno=retorno)





        # return formulario
        # return formulario["pergunta"]



# persona = PersonaBuilder()
# persona.m_add_contexto_profissao("Professo de história do ensino fundamental do brasil da quarta série")
# persona.m_add_contexto_ambiente_or_tecnologias("receber material para realizar uma aula de 2 horas")

# gpt_api = GptApi()
# retorno = gpt_api.m_conversa(persona=persona, pergunta="sobre maurissio de nassau")
# retorno = markdown.markdown(retorno)
# return render_template("gpt.html", retorno=retorno)












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



@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        verify_token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if verify_token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return 'Verificação falhou', 403

    if request.method == 'POST':
        message = request.json

        # Processar a mensagem recebida
        print('Mensagem recebida:', message)

        # Responder à mensagem (opcional)
        phone_number = message['entry'][0]['changes'][0]['value']['messages'][0]['from']
        reply_message = 'Obrigado pela sua mensagem!'

        response_data = {
            'messaging_product': 'whatsapp',
            'to': phone_number,
            'text': {'body': reply_message}
        }

        response = requests.post(
            f'https://graph.facebook.com/v11.0/me/messages?access_token={ACCESS_TOKEN}',
            json=response_data
        )

        if response.status_code == 200:
            print('Resposta enviada com sucesso!')
        else:
            print('Erro ao enviar resposta:', response.text)
        return 'EVENT_RECEIVED', 200





if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug= "--debug")