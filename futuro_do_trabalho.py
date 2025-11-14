import requests
import json
from dotenv import load_dotenv
import http.client
import os

load_dotenv()

conn = http.client.HTTPSConnection("jsearch.p.rapidapi.com")

API_KEY = os.getenv('rapidapi-key')
API_HOST = os.getenv('rapidapi-host')

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}


conn.request("GET", "/search?query=developer%20jobs%20in%20chicago&page=1&num_pages=1&country=us&date_posted=all", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


def obter_tendencias_vagas ():
    """
    Faz uma requisição para a API JSearch (RapidAPI)
    e retorna uma lista de dicionários padronizados.
    """

    url = API_HOST

    # TODO 2: Configurar os parâmetros da requisição
    # Esses parâmetros definem o termo buscado, país etc.
    querystring = {
        # "query": "developer",   # exemplo de busca
        # Você vai decidir o termo que vai usar
    }

    # TODO 3: Colocar os headers obrigatórios da RapidAPI
    headers = {
        "x-rapidapi-key": "SUA_CHAVE_AQUI",
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }

    try:
        # TODO 4: Fazer a requisição usando requests.get()
        # Exemplo:
        # response = requests.get(url, headers=headers, params=querystring)
        pass

        # TODO 5: Converter resposta para JSON
        # dados = response.json()

        # TODO 6: Acessar a lista de resultados dentro do JSON
        # A JSearch normalmente retorna dentro do campo "data"
        # lista_profissoes = dados["data"]

        # TODO 7: Padronizar cada profissão em um novo dicionário
        # com os campos que VOCÊS definiram no planejamento.
        profissões_formatadas = []

        # Laço para percorrer os resultados:
        # for item in lista_profissoes:
        #     profissao = {
        #         "titulo": item.get("job_title"),
        #         "empresa": item.get("employer_name"),
        #         "local": item.get("job_city"),
        #
        #         # ATENÇÃO: A API NÃO TEM taxa de crescimento!
        #         # VOCÊS precisam criar uma lógica para gerar esse valor.
        #         "crescimento": ???  
        #     }
        #
        #     profissões_formatadas.append(profissao)

        # return profissões_formatadas

    except Exception as erro:
        print("Erro ao acessar a API:", erro)
    return []



def filtrar_vagas(lista_vagas):
    """
Recebe a lista de profissões e retorna somente
as consideradas promissoras.
Vocês definem o critério.
"""

# TODO: definir critério de filtro e retornar nova lista
# Exemplo de lógica:
# return [p for p in lista_profissoes if p["crescimento"] > 5]
pass





def calcular_crescimento_total(profissoes):
    """
    Soma recursivamente a taxa de crescimento
    de todas as profissões da lista.
    """

    # TODO: implementar a lógica recursiva:
    # - Caso base: quando indice >= len(lista)
    # - Caso recursivo: valor atual + chamada para o próximo índice
    pass




def exibir_profissoes(lista_profissoes):
    """
    Exibe, no console, as profissões e suas informações.
    """

    # TODO: usar laço for para imprimir os dados
    # Exemplo:
    # for p in lista_profissoes:
    #     print("Profissão:", p["titulo"])
    #     print("Empresa:", p["empresa"])
    #     print("Local:", p["local"])
    #     print("Crescimento:", p["crescimento"])
    #     print("-" * 30)
    pass




def main ():
    print("\n=== FUTURO DO TRABALHO - GLOBAL SOLUTION ===\n")

    # 1. Obter dados da API
    profissoes = obter_tendencias_emprego()

    # 2. Perguntar ao usuário
    termo = input("Digite uma profissão para buscar: ")

    # (Vocês podem usar esse termo para fazer outra busca
    # ou só para mostrar resultados que combinem com o termo)

    # 3. Filtrar profissões
    filtradas = filtrar_profissoes(profissoes)

    # 4. Exibir informações
    exibir_profissoes(filtradas)

    # 5. Calcular crescimento total
    total = calcular_crescimento_total(filtradas)
    print("Crescimento total das profissões filtradas:", total)

if __name__ == '__main__':
    main()