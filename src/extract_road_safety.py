import pandas as pd
import os
import re

RAW_FILE = "data/raw/eu_table.html"

def limpar_nome_coluna(col):
    # Remove referências tipo [26]
    col = re.sub(r"\[\d+\]", "", col)
    return col.strip()

def main():
    df = pd.read_html(RAW_FILE)[0]

    # Limpar nomes das colunas
    df.columns = [limpar_nome_coluna(col) for col in df.columns]

    # Colunas exigidas no desafio
    df = df[[
        "Country",
        "Area (thousands of km2)",
        "Population in 2018",
        "GDP per capita in 2018",
        "Population density (inhabitants per km2) in 2017",
        "Vehicle ownership (per thousand inhabitants) in 2016",
        "Total Road Deaths in 2018",
        "Road deaths per Million Inhabitants in 2018"
    ]]

    # Adicionar coluna Year
    df.insert(1, "Year", 2018)

    # Renomear para o formato solicitado
    df.columns = [
        "Country",
        "Year",
        "Area",
        "Population",
        "GDP per capita",
        "Population density",
        "Vehicle ownership",
        "Total road deaths",
        "Road deaths per Million Inhabitants"
    ]

    # Ordenar pela coluna pedida
    df = df.sort_values(by="Road deaths per Million Inhabitants")

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/road_safety_eu.csv", index=False)

    print("CSV gerado com sucesso!")

if __name__ == "__main__":
    main()