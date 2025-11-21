# Projeto: Análise de Tendências do Futuro do Trabalho - Insight Jobs

Este projeto consiste em um *script* Python para analisar tendências de vagas de emprego, utilizando a **JSearch API** através da plataforma RapidAPI. O objetivo é simular a busca por oportunidades de trabalho, filtrar os resultados e calcular um índice de "crescimento" potencial para as vagas encontradas.

## 👥 Integrantes do Grupo

| Nome | Matrícula |
| :--- | :--- |
| Joao Basta | 565383 |
| Pedro Almeida | 564711 |
| Kelwin SIlva | 566348 |

## 💡 Explicação do Projeto

O arquivo principal, `futuro_do_trabalho.py`, é uma ferramenta de linha de comando que realiza as seguintes operações:

1.  **Busca de Vagas:** Conecta-se à JSearch API (RapidAPI) para buscar vagas de emprego com base em um termo de pesquisa fornecido.
2.  **Processamento de Dados:** Formata os dados brutos da API em um dicionário padronizado, incluindo campos como título, empresa, local, modalidade e tipo de contratação.
3.  **Cálculo de Crescimento:** Atribui um valor aleatório de 1 a 10 para o campo `crescimento` de cada vaga e, em seguida, utiliza uma função **recursiva** (`calcular_crescimento_total`) para somar o índice de crescimento de todas as vagas filtradas.
4.  **Filtragem:** Permite aplicar um filtro opcional nos resultados da busca (título, empresa ou local).
5.  **Saída JSON:** Retorna o resultado final (total de vagas, lista de vagas e o índice de crescimento total) em formato JSON para fácil integração com outros sistemas.

O projeto demonstra o uso de:
*   Requisições HTTP com a biblioteca `requests`.
*   Gestão de segredos (chaves de API) com variáveis de ambiente e o arquivo `.env` (biblioteca `python-dotenv`).
*   Estruturas de dados e algoritmos, como a função recursiva para agregação de dados.

## 🛠️ Como Testar e Executar

Para executar o projeto, você precisará ter o Python instalado e configurar suas chaves de API.

### 1. Pré-requisitos

*   **Python 3.x**
*   **Chave de API:** Uma chave válida para a **JSearch API** no RapidAPI.

### 2. Instalação de Dependências

Instale as bibliotecas Python necessárias usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Configuração das Variáveis de Ambiente

O script requer duas variáveis de ambiente para autenticação na RapidAPI. Crie um arquivo chamado `.env` na mesma pasta do script `futuro_do_trabalho.py` e adicione suas chaves:

```
# Conteúdo do arquivo .env
rapidapi-key="SUA_CHAVE_AQUI"
rapidapi-host="jsearch.p.rapidapi.com"
```

**Nota:** Substitua `"SUA_CHAVE_AQUI"` pela sua chave real da RapidAPI.

### 4. Execução do Script

O script é executado via linha de comando, aceitando um termo de busca obrigatório e um termo de filtro opcional.

#### **Caso 1: Busca Simples**

Busca por vagas relacionadas a "Desenvolvedor Python":

```bash
python futuro_do_trabalho.py "Desenvolvedor Python"
```

#### **Caso 2: Busca com Filtro**

Busca por vagas relacionadas a "Desenvolvedor Python" e filtra os resultados para incluir apenas as vagas da "Google":

```bash
python futuro_do_trabalho.py "Desenvolvedor Python" "Google"
```

### 5. Saída Esperada

A saída do script será um objeto JSON impresso no console, contendo os resultados da busca e o cálculo do crescimento total.

```json
{
    "total_vagas": 10,
    "vagas": [
        {
            "titulo": "Desenvolvedor Python Sênior",
            "empresa": "TechCorp",
            "local": "São Paulo",
            "plataforma": "LinkedIn",
            "modalidade": false,
            "salario": "Não informado",
            "tipo_carga_horaria": "fulltime",
            "beneficios": null,
            "crescimento": 7
        },
        // ... outras vagas
    ],
    "crescimento_total": 55,
    "termo_busca": "Desenvolvedor Python",
    "termo_filtro": ""
}
```

