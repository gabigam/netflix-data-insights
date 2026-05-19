# ==========================================
# Netflix Catalog — Exploratory Data Analysis
# ==========================================
# Objetivo:
# Explorar o catálogo da Netflix e extrair
# insights sobre crescimento, países produtores,
# tipos de conteúdo e tendências do catálogo.
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. CARREGAMENTO DOS DADOS
# --------------------------------------------------

print("\nCarregando dataset...")
df = pd.read_csv("netflix_titles.csv")

print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
print("\nPrimeiras linhas:")
print(df.head())


# --------------------------------------------------
# 2. LIMPEZA E PREPARAÇÃO DOS DADOS
# --------------------------------------------------

print("\nTratando dados...")

# Conversão de datas
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

# Tratamento de valores ausentes
df["country"] = df["country"].fillna("Not informed")
df["director"] = df["director"].fillna("Not informed")

# Separação de listas (países e gêneros vêm separados por vírgula)
df["country"] = df["country"].str.split(",")
df["listed_in"] = df["listed_in"].str.split(",")

print("Tratamento concluído.")


# --------------------------------------------------
# 3. PAÍSES COM MAIOR PRODUÇÃO DE CONTEÚDO
# --------------------------------------------------

print("\nAnalisando países com mais títulos...")

countries = df.explode("country")
top_countries = countries["country"].value_counts().head(10)

plt.figure()
top_countries.plot(kind="bar")
plt.title("Top 10 países com mais títulos no catálogo")
plt.ylabel("Quantidade de títulos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 4. CRESCIMENTO DO CATÁLOGO (FILMES vs SÉRIES)
# --------------------------------------------------

print("Analisando crescimento do catálogo...")

growth = df.groupby(["year_added", "type"]).size().unstack()

plt.figure()
growth.plot()
plt.title("Evolução de títulos adicionados por ano")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 5. GÊNEROS MAIS FREQUENTES
# --------------------------------------------------

print("Analisando gêneros mais comuns...")

genres = df.explode("listed_in")
top_genres = genres["listed_in"].value_counts().head(10)

plt.figure()
top_genres.plot(kind="bar")
plt.title("Gêneros mais frequentes no catálogo")
plt.ylabel("Quantidade de títulos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 6. TENDÊNCIA DE LANÇAMENTOS AO LONGO DO TEMPO
# --------------------------------------------------

print("Analisando tendência de lançamentos...")

release_trend = df["release_year"].value_counts().sort_index()

plt.figure()
release_trend.plot()
plt.title("Quantidade de conteúdos por ano de lançamento")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 7. INSIGHTS FINAIS
# --------------------------------------------------

print("\n================ INSIGHTS ================\n")

print("• O volume de títulos cresce rapidamente a partir de 2015.")
print("• Filmes representam a maior parte do catálogo.")
print("• Estados Unidos lideram a produção de conteúdo.")
print("• Gêneros de Drama e Comédia aparecem com maior frequência.")

print("\nAnálise finalizada.")