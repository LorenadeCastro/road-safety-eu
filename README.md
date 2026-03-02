## 🚗 Desafio Técnico — Road Safety EU (Data Package + Visualização)

📌 Descrição do Desafio

O objetivo do desafio foi:

1. Extrair dados públicos sobre mortes no trânsito na União Europeia
2. Organizar os dados em formato estruturado
3. Transformar o repositório em um Data Package
4. Construir ao menos um gráfico gerando um insight a partir dos dados

🧠 Estratégia de Solução

Para resolver o desafio, foram seguidos os seguintes passos:

1️⃣ Extração de Dados

Os dados foram obtidos da página da Wikipedia:
List of countries by traffic-related death rate (2018)

Foi utilizado:
```
requests para obter o HTML
```
```
pandas.read_html() para extrair a tabela
```
```
Limpeza das colunas (remoção de referências como [26], [27])
```
```
Padronização de valores numéricos
```

2️⃣ Tratamento e Limpeza

Foram realizadas as seguintes etapas:
```
Remoção de notas de rodapé
```
```
Conversão de colunas numéricas
```
```
Padronização de nomes
```
```
Organização das colunas relevantes
```
```
Exportação para CSV limpo
```

Arquivo gerado:
```
data/processed/road_safety_eu.csv
```

3️⃣ Transformação em Data Package

O projeto foi estruturado seguindo o padrão Frictionless Data.

Arquivo gerado:
```
data/processed/datapackage.json
```

O Data Package contém:
```
Metadados do dataset
```
```
Descrição da fonte
```
```
Schema com tipos de dados
```
```
Estrutura organizada para reutilização
```
```
Campos disponíveis:
```
```
Country
```
```
Year
```
```
Area
```
```
Population
```
```
GDP per capita
```
```
Population density
```
```
Vehicle ownership
```
```
Total road deaths
```
```
Road deaths per Million Inhabitants
```

4️⃣ Análise e Visualização

Foram criadas duas visualizações principais:

📊 Top 10 países com mais mortes no trânsito (2018)

Permite identificar os países com maior número absoluto de mortes.

📈 Relação entre PIB per capita e mortes por milhão

Permite observar um padrão interessante:

Países com menor PIB per capita tendem a apresentar maiores taxas de mortalidade no trânsito.

Os gráficos são salvos em:
```
data/processed/
```

📁 Estrutura Final do Projeto
```
road-safety-eu/
│
├── data/
│   ├── raw/
│   │   └── eu_table.html
│   └── processed/
│       ├── road_safety_eu.csv
│       ├── top10_deaths.png
│       ├── gdp_vs_deaths.png
│       └── datapackage.json
│
├── src/
│   ├── extract_road_safety.py
│   └── analysis.py
│
├── requirements.txt
└── README.md
```

⚙️ Como Executar o Projeto

1️⃣ Criar ambiente virtual
```
python -m venv venv
```
Ativar no Windows:
```
venv\Scripts\activate
```
2️⃣ Instalar dependências
```
pip install -r requirements.txt
```
3️⃣ Executar extração
```
python src/extract_road_safety.py
```
4️⃣ Executar análise
```
python src/analysis.py
```

📊 Insight Gerado

A análise indica que:

Países do leste europeu apresentam maiores taxas de mortalidade por milhão.

Existe relação inversa entre desenvolvimento econômico (PIB per capita) e segurança viária.

Países com maior investimento e infraestrutura tendem a apresentar menores taxas de mortalidade.

🎯 Objetivos do Desafio Atendidos
```
✔ Extração automatizada
```
```
✔ Limpeza e tratamento de dados
```
```
✔ Organização como Data Package
```
```
✔ Geração de visualização
```
```
✔ Identificação de insight relevante
```

🛠 Tecnologias Utilizadas
```
Python 3.12
```
```
Pandas
```
```
Requests
```
```
BeautifulSoup
```
```
LXML
```
```
Matplotlib
```

👩‍💻 Autora:
Lorena de Castro Rocha Gonçalves

Estudante de Análise e Desenvolvimento de Sistemas

