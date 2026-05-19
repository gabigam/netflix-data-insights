import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Netflix Data Insights",
    page_icon="🎬",
    layout="wide"
)

# =====================================================
# Carregamento e preparação dos dados
# =====================================================
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")

    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["year_added"] = df["date_added"].dt.year
    df["country"] = df["country"].fillna("Unknown")

    return df

df = load_data()

# =====================================================
# Título e contexto
# =====================================================
st.title("🎬 Netflix Data Insights")
st.write(
    """
    Este dashboard explora tendências do catálogo da Netflix com base
    no dataset público disponível no Kaggle (snapshot até 2021).
    """
)

# =====================================================
# Filtros laterais
# =====================================================
st.sidebar.header("Filtros")

content_type = st.sidebar.multiselect(
    "Tipo de conteúdo",
    options=df["type"].unique(),
    default=df["type"].unique()
)

year_range = st.sidebar.slider(
    "Ano de lançamento",
    int(df["release_year"].min()),
    int(df["release_year"].max()),
    (2015, 2021)
)

filtered_df = df[
    (df["type"].isin(content_type)) &
    (df["release_year"].between(year_range[0], year_range[1]))
]

# =====================================================
# Indicadores principais
# =====================================================
st.subheader("Visão geral do catálogo")

col1, col2, col3 = st.columns(3)

col1.metric("Títulos analisados", len(filtered_df))
col2.metric("Total de filmes", len(filtered_df[filtered_df["type"] == "Movie"]))
col3.metric("Total de séries", len(filtered_df[filtered_df["type"] == "TV Show"]))

st.divider()

# =====================================================
# Distribuição Filmes vs Séries
# =====================================================
st.subheader("Filmes x Séries no catálogo")

type_count = filtered_df["type"].value_counts()

fig1 = plt.figure()
type_count.plot(kind="bar")
plt.xticks(rotation=0)
plt.ylabel("Quantidade de títulos")
st.pyplot(fig1)

st.caption(
    "Observa-se que a Netflix historicamente adiciona mais filmes do que séries."
)

# =====================================================
# Países com mais produções
# =====================================================
st.subheader("Países com maior presença no catálogo")

countries = (
    filtered_df["country"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)

fig2 = plt.figure()
countries.plot(kind="bar")
plt.xticks(rotation=45)
plt.ylabel("Quantidade de títulos")
st.pyplot(fig2)

st.caption(
    "Os Estados Unidos lideram com folga, seguidos por Índia e Reino Unido."
)

# =====================================================
# Crescimento ao longo dos anos
# =====================================================
st.subheader("Evolução do catálogo ao longo do tempo")

year_growth = filtered_df["release_year"].value_counts().sort_index()

fig3 = plt.figure()
year_growth.plot()
plt.ylabel("Títulos lançados")
st.pyplot(fig3)

st.caption(
    "O crescimento acelera após 2015, período de expansão global da plataforma."
)

st.divider()

st.markdown(
    """
    **Sobre o projeto**

    Este projeto foi desenvolvido como parte do meu portfólio de análise de dados,
    com foco em exploração, limpeza e visualização de dados utilizando Python,
    Pandas e Streamlit.
    """
)