import streamlit as st
st.set_page_config(page_title="Plano de Negócios - WOHS", page_icon="📋", layout="wide")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

st.title("📋 Plano de Negócios – WOHS")
st.markdown("Preencha o plano passo a passo, visualize gráficos e exporte tudo.")

# Abas principais
aba_empresa, aba_objetivos, aba_financas, aba_dashboard, aba_exportar = st.tabs([
    "🏢 Sobre a Empresa", "🎯 Objetivos & Estratégia", "📈 Projeções Financeiras", "📊 Dashboard", "📤 Exportar Plano"
])

# --- ABA 1: Empresa ---
with aba_empresa:
    st.subheader("🏢 Informações da Empresa")
    nome = st.text_input("Nome da Empresa", "WOHS")
    missao = st.text_area("Missão")
    visao = st.text_area("Visão")
    valores = st.text_area("Valores e Cultura")
    publico_alvo = st.text_input("Público-Alvo")
    proposta_valor = st.text_area("Proposta de Valor")

# --- ABA 2: Objetivos ---
with aba_objetivos:
    st.subheader("🎯 Metas e Estratégia")
    metas_curto = st.text_area("Metas de curto prazo")
    metas_longo = st.text_area("Metas de longo prazo")
    estrategia = st.text_area("Estratégias de crescimento")
    canais = st.text_area("Canais de vendas e marketing")

# --- ABA 3: Finanças ---
with aba_financas:
    st.subheader("📈 Projeções Financeiras")
    receita_mensal = st.number_input("Receita Mensal Estimada (€)", min_value=0.0, step=100.0)
    custos_fixos = st.number_input("Custos Fixos Mensais (€)", min_value=0.0, step=50.0)
    custos_variaveis = st.number_input("Custos Variáveis Mensais (€)", min_value=0.0, step=50.0)
    lucro = receita_mensal - custos_fixos - custos_variaveis
    st.metric("💰 Lucro Mensal Estimado", f"€{lucro:,.2f}")

# --- ABA 4: Dashboard ---
with aba_dashboard:
    st.subheader("📊 Dashboard Financeiro")

    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
    receitas = [receita_mensal] * 6
    custos = [(custos_fixos + custos_variaveis)] * 6
    lucros = [r - c for r, c in zip(receitas, custos)]

    fig = go.Figure()
    fig.add_trace(go.Bar(name="Receita", x=meses, y=receitas, marker_color='green'))
    fig.add_trace(go.Bar(name="Custos", x=meses, y=custos, marker_color='red'))
    fig.add_trace(go.Scatter(name="Lucro", x=meses, y=lucros, mode='lines+markers', line=dict(color='blue', width=4)))

    fig.update_layout(
        barmode='group',
        title="📊 Receita, Custos e Lucro nos Próximos 6 Meses",
        xaxis_title="Mês",
        yaxis_title="€",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

# --- ABA 5: Exportar ---
with aba_exportar:
    st.subheader("📤 Exportar Plano de Negócios")
    st.warning("🚧 Funcionalidade de exportação em construção. Vamos ativar em breve!")
