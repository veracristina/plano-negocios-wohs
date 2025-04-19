import streamlit as st
st.set_page_config(page_title="Plano de Negócios - WOHS", page_icon="📋", layout="wide")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from io import BytesIO

st.title("📋 Plano de Negócios – WOHSBRAND")
st.markdown("Preencha o plano passo a passo, visualize gráficos e exporte tudo.")

# Abas principais
aba_empresa, aba_objetivos, aba_financas, aba_custos, aba_dashboard, aba_exportar = st.tabs([
    "🏢 Sobre a Empresa", "🎯 Objetivos & Estratégia", "📈 Projeções Financeiras", "💸 Detalhe de Custos", "📊 Dashboard", "📤 Exportar Plano"
])


# --- ABA 1: Empresa ---
with aba_empresa:
    st.subheader("🏢 Informações da Empresa")
    nome = st.text_input("Nome da Empresa", "WOHSBRAND")
    missao = st.text_area("Missão", "Inspirar atletas híbridos a viverem com intenção, superação e estilo.")
    visao = st.text_area("Visão", "Ser a marca referência na cultura atlética híbrida em Portugal e além.")
    valores = st.text_area("Valores e Cultura", "Autenticidade, disciplina, liberdade, inovação e comunidade.")
    publico_alvo = st.text_input("Público-Alvo", "Jovens atletas híbridos (20–40 anos) que valorizam treino, estilo e comunidade.")
    proposta_valor = st.text_area("Proposta de Valor", "Mais do que roupa, criamos experiências e uma cultura. Camps, competições e vestuário com identidade atlética forte.")

# --- ABA 2: Objetivos ---
with aba_objetivos:
    st.subheader("🎯 Metas e Estratégia")
    metas_curto = st.text_area("Metas de curto prazo", "- Lançar nova coleção\n- Realizar 2 WOHS Training Camps\n- Ampliar presença nas redes e eventos")
    metas_longo = st.text_area("Metas de longo prazo", "- Abrir loja física em Lisboa\n- Parcerias com boxes e atletas\n- Expandir para eventos internacionais")
    estrategia = st.text_area("Estratégias de crescimento", "- Drops sazonais ligados a eventos\n- Marketing de influência\n- Colabs com artistas e marcas independentes")
    canais = st.text_area("Canais de vendas e marketing", "Instagram, TikTok, loja online, eventos desportivos, parcerias com ginásios e coaches")

# --- ABA 3: Finanças ---
with aba_financas:
    st.subheader("📈 Projeções Financeiras")
    receita_mensal = st.number_input("Receita Mensal Estimada (€)", min_value=0.0, step=100.0, value=12000.0)
    custos_fixos = st.number_input("Custos Fixos Mensais (€)", min_value=0.0, step=50.0, value=4000.0)
    custos_variaveis = st.number_input("Custos Variáveis Mensais (€)", min_value=0.0, step=50.0, value=3000.0)
    lucro = receita_mensal - custos_fixos - custos_variaveis
    st.metric("💰 Lucro Mensal Estimado", f"€{lucro:,.2f}")

# --- ABA 4: Detalhe de Custos ---
with aba_custos:
    st.subheader("💸 Detalhe de Custos Fixos e Variáveis")

    st.markdown("### ✏️ Inputs de Custos Fixos")

    email = st.number_input("Email / mês", value=4.48, step=0.01)
    site_anual = st.number_input("Custo anual do site", value=29.90, step=0.01)
    contabilista = st.number_input("Contabilista / mês", value=100.0)
    comissao_banco = st.number_input("Comissão bancária / mês", value=9.0)

    st.markdown("#### Marketing Mensal")
    mkt_meses_1a3 = st.number_input("💰 Marketing Baldaya", value=1200.0)
    mkt_meses_4a6 = st.number_input("💰 Mkt (a partir do mês 4)", value=100.0)

    st.markdown("### ✏️ Custos Variáveis Estimados")
    variaveis_mensais = st.number_input("Custos Variáveis Estimados / mês", value=3000.0)

    meses = ["Mês 1", "Mês 2", "Mês 3", "Mês 4", "Mês 5", "Mês 6"]
    tabela_custos = []

    for i in range(6):
        mkt = mkt_meses_1a3 if i < 3 else mkt_meses_4a6
        site_mensal = site_anual / 12

        total_fixos = email + mkt + site_mensal + contabilista + comissao_banco
        total_mes = total_fixos + variaveis_mensais

        tabela_custos.append({
            "Mês": meses[i],
            "Fixos (€)": round(total_fixos, 2),
            "Variáveis (€)": round(variaveis_mensais, 2),
            "Total (€)": round(total_mes, 2)
        })

    df_custos = pd.DataFrame(tabela_custos)

    st.markdown("### 📋 Tabela de Custos (6 Meses)")
    st.dataframe(df_custos.style.format({
        "Fixos (€)": "€{:.2f}",
        "Variáveis (€)": "€{:.2f}",
        "Total (€)": "€{:.2f}"
    }), use_container_width=True)

    st.markdown("### 📊 Gráfico de Custos Totais")
    fig_custos = px.bar(df_custos, x="Mês", y=["Fixos (€)", "Variáveis (€)"],
                        title="Custos Fixos e Variáveis por Mês",
                        barmode="stack", text_auto=".2s")
    st.plotly_chart(fig_custos, use_container_width=True)

        # Gráfico de Pizza: Distribuição de Custos
    st.markdown("### 🥧 Distribuição de Custos Fixos e Variáveis")
    labels = ['Custos Fixos', 'Custos Variáveis']
    values = [df_custos['Fixos (€)'].sum(), df_custos['Variáveis (€)'].sum()]
    fig_pizza = px.pie(names=labels, values=values, title='Distribuição de Custos')
    st.plotly_chart(fig_pizza, use_container_width=True)




# --- ABA 5: Dashboard ---
with aba_dashboard:
    st.subheader("📊 Dashboard Financeiro")

    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
    receitas = [receita_mensal] * 6
    custos_fixos_mensal = [email + (mkt_meses_1a3 if i < 3 else mkt_meses_4a6) + (site_anual / 12) + contabilista + comissao_banco for i in range(6)]
    custos_variaveis_mensal = [variaveis_mensais] * 6
    lucros = [r - f - v for r, f, v in zip(receitas, custos_fixos_mensal, custos_variaveis_mensal)]

    # Tabela Balanço
    df_balanco = pd.DataFrame({
        "Mês": meses,
        "Receita (€)": receitas,
        "Custos Fixos (€)": custos_fixos_mensal,
        "Custos Variáveis (€)": custos_variaveis_mensal,
        "Lucro (€)": lucros
    })

    df_balanco["Margem (%)"] = (df_balanco["Lucro (€)"] / df_balanco["Receita (€)"]) * 100

    # Gráfico de barras
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Receita", x=meses, y=receitas, marker_color='green'))
    fig.add_trace(go.Bar(name="Custos Totais", x=meses, y=[f+v for f, v in zip(custos_fixos_mensal, custos_variaveis_mensal)], marker_color='red'))
    fig.add_trace(go.Scatter(name="Lucro", x=meses, y=lucros, mode='lines+markers', line=dict(color='blue', width=4)))
    fig.update_layout(
        barmode='group',
        title="📊 Receita, Custos e Lucro nos Próximos 6 Meses",
        xaxis_title="Mês",
        yaxis_title="€",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Tabela com margem
    st.markdown("### 📊 Balanço Mensal Contabilístico")
    st.dataframe(df_balanco.style.format({
        "Receita (€)": "€{:.2f}",
        "Custos Fixos (€)": "€{:.2f}",
        "Custos Variáveis (€)": "€{:.2f}",
        "Lucro (€)": "€{:.2f}",
        "Margem (%)": "{:.2f}%"
    }), use_container_width=True)



# --- ABA 6: Exportar ---
with aba_exportar:
    # Exportação para Excel
    st.markdown("### 📤 Exportar Plano de Negócios para Excel")
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        # Dados da Empresa
        df_empresa = pd.DataFrame({
            'Campo': ['Nome', 'Missão', 'Visão', 'Valores e Cultura', 'Público-Alvo', 'Proposta de Valor'],
            'Informação': [nome, missao, visao, valores, publico_alvo, proposta_valor]
        })
        df_empresa.to_excel(writer, sheet_name='Empresa', index=False)

        # Objetivos e Estratégia
        df_objetivos = pd.DataFrame({
            'Campo': ['Metas de Curto Prazo', 'Metas de Longo Prazo', 'Estratégias de Crescimento', 'Canais de Vendas e Marketing'],
            'Informação': [metas_curto, metas_longo, estrategia, canais]
        })
        df_objetivos.to_excel(writer, sheet_name='Objetivos', index=False)

        # Projeções Financeiras
        df_financas = pd.DataFrame({
            'Campo': ['Receita Mensal Estimada (€)', 'Custos Fixos Mensais (€)', 'Custos Variáveis Mensais (€)', 'Lucro Mensal Estimado (€)'],
            'Valor': [receita_mensal, custos_fixos, custos_variaveis, lucro]
        })
        df_financas.to_excel(writer, sheet_name='Finanças', index=False)

        # Detalhe de Custos
        df_custos.to_excel(writer, sheet_name='Detalhe de Custos', index=False)

        # Balanço Mensal
        df_balanco = pd.DataFrame({
            'Mês': meses,
            'Receita (€)': receitas,
            'Custos Fixos (€)': [email + (mkt_meses_1a3 if i < 3 else mkt_meses_4a6) + (site_anual / 12) + contabilista + comissao_banco for i in range(6)],
            'Custos Variáveis (€)': [variaveis_mensais] * 6,
            'Lucro (€)': [receitas[i] - (email + (mkt_meses_1a3 if i < 3 else mkt_meses_4a6) + (site_anual / 12) + contabilista + comissao_banco) - variaveis_mensais for i in range(6)]
        })
        df_balanco.to_excel(writer, sheet_name='Balanço Mensal', index=False)

        
        output.seek(0)
        st.download_button(
            label="📥 Baixar Plano de Negócios (Excel)",
            data=output,
            file_name='plano_negocios_wohs.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
