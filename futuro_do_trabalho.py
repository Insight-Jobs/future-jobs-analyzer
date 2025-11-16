import requests
import json
from dotenv import load_dotenv
import http.client
import os

load_dotenv()

API_KEY = os.getenv('rapidapi-key')
API_HOST = os.getenv('rapidapi-host')

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}


def obter_tendencias_vagas (termo_busca):
    """
    Faz uma requisição para a API JSearch (RapidAPI)
    e retorna uma lista de dicionários padronizados.
    """

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
       "query": termo_busca,
        "page": "1",
        "num_pages": "1",
        "country": "br"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        

        dados = response.json()

        lista_vagas = dados["data"]

        vagas_formatadas = []

        for item in lista_vagas:
            vaga ={
                 "titulo": item.get("job_title"),
                 "empresa": item.get("employer_name"),
                 "local": item.get("job_city"),
                 "plataforma": item.get("publisher"),
                 "modalidade": item.get("job_is_remote"),
                 "salario": item.get ("job_salary", "Não informado"),
                 "tipo de carga horaria": item.get("job_employment_type"),
                 "beneficios": item.get ("Benefits")
            } 

            vagas_formatadas.append(vaga)

        return vagas_formatadas

    except Exception as erro:
        print("Erro ao acessar a API:", erro)
    return []



def filtrar_vagas(lista_vagas, termo_filtro):
    """
    Recebe a lista de profissões e retorna somente
    as consideradas promissoras.
    Vocês definem o critério.
    """
    vagas_filtradas=[]
    termo = termo_filtro.lower()

    for vaga in lista_vagas:
        titulo = str(vaga["titulo"]).lower()
        empresa = str(vaga["empresa"]).lower()
        local = str(vaga["local"]).lower()

        if termo in titulo or termo in empresa or termo in local:
            vagas_filtradas.append(vaga)

    return vagas_filtradas


def calcular_crescimento_total(lista_vagas, indice = 0):
    """
    Soma recursivamente a taxa de crescimento
    de todas as profissões da lista.
    """

       # Caso base: chegou no fim da lista
    if indice == len(lista_vagas):
        return 0

    # Pega o valor de crescimento da vaga atual
    crescimento_atual = lista_vagas[indice].get("crescimento", 0)

    # Caso recursivo: valor atual + restante da lista
    return crescimento_atual + calcular_crescimento_total(lista_vagas, indice + 1)




def exibir_vagas(lista_profissoes):
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
    termo_busca = input("Digite o que deseja buscar (ex: developer, data analyst, nurse): ")

    vagas = obter_tendencias_vagas()

    print(f"\nForam encontradas {len(vagas)} vagas.")

    termo_filtro = input("Digite um termo para filtrar os resultados (ou deixe vazio para não filtrar): ")
    if termo_filtro.strip() != "":
            vagas = filtrar_vagas(vagas, termo_filtro)

    print(f"\nVagas após filtro: {len(vagas)}\n")
    exibir_vagas(vagas)

if __name__ == '__main__':
    main()