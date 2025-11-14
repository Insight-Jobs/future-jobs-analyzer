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


def obter_tendencias_vagas ():
    """
    Faz uma requisição para a API JSearch (RapidAPI)
    e retorna uma lista de dicionários padronizados.
    """

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
       "query": "desenvolvedor",
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