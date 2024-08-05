import tiktoken


class ContadorToken():
    def __init__(self) -> None:
        self.MODEL_GTP_4o = {
            'modelo' : "gpt-4o", 
            'custo': 5.0 / 1000000, 
            'custo_out': 15.0 / 1000000
        }
        self.MODEL_GTP_3_5_TURBO_1106 = {
            'modelo' : "gpt-3.5-turbo-0125", 
            'custo': 0.5 / 1000000, 
            'custo_out': 1.5 / 1000000
        }
        
    def m_calc(self, msg, modelo):
        print(msg)
        print(modelo.get('modelo'))
        print(modelo.get('custo'))
        codificador = tiktoken.encoding_for_model( modelo.get('modelo') )
        lista_tokens = codificador.encode( msg )
        return f'''Custo do Token: {len(lista_tokens) * modelo.get('custo')} '''   # lista_tokens


        # codificador = tiktoken.encoding_for_model(modelo)
        # lista_tokens = codificador.encode(texto)
        # return lista_tokens

    # def m_calcular(mensagem, modelo, custo_por_k):
    #     print(mensagem)
    #     print(modelo)
    #     print(custo_por_k)

        # codificador = tiktoken.encoding_for_model(modelo)
        # lista_tokens = codificador.encode(texto)
        # return lista_tokens


#         print("Lista de Tokens: ", lista_tokens)
#         print("Quantos tokens temos: ", len(lista_tokens))
#         print(f"Custo para o modelo {modelo} é de ${(len(lista_tokens)/1000) * custo_por_k}")

#         #1TRABALHANDO AQUI
#         # modelo = "gpt-4"
#         codificador = tiktoken.encoding_for_model(modelo)
#         lista_tokens = codificador.encode("Você é um categorizador de produtos.")

# print("Lista de Tokens: ", lista_tokens)
# print("Quantos tokens temos: ", len(lista_tokens))
# print(f"Custo para o modelo {modelo} é de ${(len(lista_tokens)/1000) * 0.03}")

# modelo = "gpt-3.5-turbo-1106"
# codificador = tiktoken.encoding_for_model(modelo)
# lista_tokens = codificador.encode("Você é um categorizador de produtos.")

# print("Lista de Tokens: ", lista_tokens)
# print("Quantos tokens temos: ", len(lista_tokens))
# print(f"Custo para o modelo {modelo} é de ${(len(lista_tokens)/1000) * 0.001}")