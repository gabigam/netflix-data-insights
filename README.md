# 🎬 Netflix Data Insights

Análise exploratória do catálogo da Netflix utilizando Python, com foco em geração de insights de negócio e visualização de dados.

Este projeto simula um cenário real de análise onde o objetivo é transformar dados brutos em informação útil para tomada de decisão.

---

## 📌 Contexto

A Netflix passou por uma grande expansão global na última década.
Utilizando um dataset público do catálogo da plataforma, este projeto investiga **como o conteúdo evoluiu ao longo do tempo** e **quais padrões podem ser observados na estratégia da empresa**.

**Cobertura dos dados:** 1925 — 2021
**Fonte:** Kaggle – Netflix Titles Dataset (snapshot público)

---

## 🎯 Perguntas de negócio

Esta análise busca responder:

* Quais países mais produzem conteúdo para a Netflix?
* O crescimento do catálogo é impulsionado por filmes ou séries?
* Como o volume de lançamentos evoluiu ao longo dos anos?
* Quais padrões podem indicar a estratégia de expansão da plataforma?

---

## 🧰 Stack utilizada

* Python
* Pandas (manipulação e limpeza de dados)
* Matplotlib (visualização)
* Streamlit (dashboard interativo)
* Análise Exploratória de Dados (EDA)

---

## 📊 Principais análises realizadas

### 🌍 Produção por país

Identificação dos países com maior presença no catálogo e análise da distribuição geográfica do conteúdo.

### 🎬 Distribuição Filmes vs Séries

Comparação entre os tipos de conteúdo disponíveis na plataforma.

### 📈 Crescimento do catálogo

Análise temporal do volume de títulos adicionados ao longo dos anos.

### 🎭 Tendências gerais do catálogo

Observação de padrões que indicam mudanças na estratégia da empresa após a expansão global.

---

## 💡 Principais insights

* A expansão do catálogo acelera significativamente após 2015
* Filmes ainda representam a maior parte do conteúdo disponível
* Estados Unidos lideram com ampla vantagem na produção
* O crescimento recente indica forte estratégia de internacionalização

---

## ⚠️ Limitações dos dados

Este dataset é um snapshot público até 2021 e não representa o catálogo atual da Netflix.
A análise tem foco em **tendências históricas**, não em dados em tempo real.

---

## 🚀 Como executar localmente

Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

Rodar a análise exploratória:

```bash
python netflix_analysis.py
```

---

## 📊 Dashboard interativo

O projeto inclui um dashboard desenvolvido em Streamlit.

Execute com:

```bash
python -m streamlit run streamlit_app.py
```

---

## 👩‍💻 Sobre o projeto

Projeto desenvolvido para portfólio de análise de dados, demonstrando habilidades em:

* limpeza e preparação de dados
* análise exploratória
* visualização
* comunicação de insights

---


