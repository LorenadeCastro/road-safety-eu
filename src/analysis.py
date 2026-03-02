import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("data/processed/road_safety_eu.csv")

    # Remover linha do total da UE
    df = df[df["Country"] != "EU 28 Total"]

    # Converter colunas numéricas corretamente
    df["GDP per capita"] = pd.to_numeric(df["GDP per capita"], errors="coerce")
    df["Road deaths per Million Inhabitants"] = pd.to_numeric(
        df["Road deaths per Million Inhabitants"], errors="coerce"
    )

    # =========================
    # 📊 GRÁFICO 1 — TOP 10 MAIS PERIGOSOS
    # =========================
    top10 = df.sort_values(
        "Road deaths per Million Inhabitants", ascending=False
    ).head(10)

    plt.figure()
    plt.barh(
        top10["Country"],
        top10["Road deaths per Million Inhabitants"]
    )
    plt.xlabel("Mortes por milhão de habitantes")
    plt.title("Top 10 países com mais mortes no trânsito (2018)")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("data/processed/top10_deaths.png")
    plt.show()

    # =========================
    # 📈 GRÁFICO 2 — PIB vs Mortes
    # =========================
    plt.figure()
    plt.scatter(
        df["GDP per capita"],
        df["Road deaths per Million Inhabitants"]
    )
    plt.xlabel("PIB per capita")
    plt.ylabel("Mortes por milhão")
    plt.title("PIB per capita vs Mortalidade no trânsito (2018)")
    plt.tight_layout()
    plt.savefig("data/processed/gdp_vs_deaths.png")
    plt.show()

    # =========================
    # 🔎 Correlação
    # =========================
    correlation = df["GDP per capita"].corr(
        df["Road deaths per Million Inhabitants"]
    )

    print("\nCorrelação PIB vs Mortes por milhão:")
    print(round(correlation, 3))


if __name__ == "__main__":
    main()