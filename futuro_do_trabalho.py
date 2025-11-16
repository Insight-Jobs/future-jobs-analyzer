import requests
import json
from dotenv import load_dotenv
import random
import os

load_dotenv()

API_KEY = os.getenv('rapidapi-key')
API_HOST = os.getenv('rapidapi-host')

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": API_HOST
}


def obter_tendencias_vagas(termo_busca):
    """
    Faz uma requisição para a API JSearch (RapidAPI)
    e retorna uma lista de dicionários padronizados.
    """

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": termo_busca,
        "page": "1",
        "num_pages": "1"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        dados = response.json()

        lista_vagas = dados.get("data", [])
        vagas_formatadas = []

        for item in lista_vagas:
            vaga = {
                "titulo": item.get("job_title"),
                "empresa": item.get("employer_name"),
                "local": item.get("job_city"),
                "plataforma": item.get("job_publisher"),
                "modalidade": item.get("job_is_remote"),
                "salario": item.get("job_salary", "Não informado"),
                "tipo_carga_horaria": item.get("job_employment_type"),
                "beneficios": item.get("job_benefits"),
                "crescimento": random.randint(1, 10)  # NECESSÁRIO para a recursão
            }

            vagas_formatadas.append(vaga)

        return vagas_formatadas

    except Exception as erro:
        print("Erro ao acessar a API:", erro)
        return []


def filtrar_vagas(lista_vagas, termo_filtro):
    """
    Filtra vagas com base no termo fornecido pelo usuário.
    """

    vagas_filtradas = []
    termo = termo_filtro.lower()

    for vaga in lista_vagas:
        titulo = str(vaga["titulo"]).lower()
        empresa = str(vaga["empresa"]).lower()
        local = str(vaga["local"]).lower()

        if termo in titulo or termo in empresa or termo in local:
            vagas_filtradas.append(vaga)

    return vagas_filtradas


def calcular_crescimento_total(lista_vagas, indice=0):
    """
    Soma recursivamente a taxa de crescimento
    de todas as vagas da lista.
    """

    # Caso base
    if indice == len(lista_vagas):
        return 0

    crescimento_atual = lista_vagas[indice].get("crescimento", 0)

    # Caso recursivo
    return crescimento_atual + calcular_crescimento_total(lista_vagas, indice + 1)


def exibir_vagas(lista_vagas):
    """
    Exibe cada vaga formatada.
    """

    for vaga in lista_vagas:
        print("Vaga:", vaga["titulo"])
        print("Empresa:", vaga["empresa"])
        print("Local:", vaga["local"])
        print("Crescimento:", vaga["crescimento"])
        print("-" * 30)


def main():
    print("\n=== FUTURO DO TRABALHO - GLOBAL SOLUTION ===\n")

    termo_busca = input("Digite o que deseja buscar (ex: developer, data analyst, nurse): ")

    vagas = obter_tendencias_vagas(termo_busca)

    print(f"\nForam encontradas {len(vagas)} vagas.")

    termo_filtro = input("Digite um termo para filtrar os resultados (ou deixe vazio para não filtrar): ")

    if termo_filtro.strip() != "":
        vagas = filtrar_vagas(vagas, termo_filtro)

    print(f"\nVagas após filtro: {len(vagas)}\n")
    exibir_vagas(vagas)

    total = calcular_crescimento_total(vagas)
    print("\nCrescimento total das vagas filtradas:", total)


if __name__ == '__main__':
    main()
