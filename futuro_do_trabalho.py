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




def filtrar_vagas(lista_vagas):






def calcular_crescimento_total(profissoes):





def exibir_profissoes(lista_profissoes):





def main ():




if __name__ == '__main__':
    main()