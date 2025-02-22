import streamlit as st
from pathlib import Path
import pandas as pd
from utilidades import leitura_dados, COMISSAO

# Logotipo
st.logo(
    Path(__file__).parents[1] / 'identidade_visual' / 'logo_completo.png',
    size='large',
    link = 'https://orenjy.com/',
    icon_image=Path(__file__).parents[1] / 'identidade_visual' / 'logo_pequeno.png',
)

#Sidebar
st.sidebar.markdown('Desenvolvido por [Orenjy](https://orenjy.com/)')

COLUNAS_ANALISE = ['filial', 'vendedor', 'produto', 'cliente_genero', 'forma_pagamento']
COLUNAS_VALOR = ['preco', 'comissao']
FUNCOES_AGG = {'soma':'sum', 'contagem':'count'}

leitura_dados()


df_vendas = st.session_state['dados']['vendas']
df_filiais = st.session_state['dados']['filiais']
df_produtos = st.session_state['dados']['produtos']


df_produtos = df_produtos.rename(columns={'nome': 'produto'})
df_vendas = df_vendas.reset_index()

df_vendas = pd.merge(left=df_vendas, 
                     right=df_produtos[['produto', 'preco']], 
                     on='produto', 
                     how='left')

df_vendas = df_vendas.set_index('data')
df_vendas['comissao'] = df_vendas['preco'] * COMISSAO

indices_selecionados = st.sidebar.multiselect('Selecione os índices para análise:', COLUNAS_ANALISE)
col_analises_filtradas = [c for c in COLUNAS_ANALISE if not c in indices_selecionados]
colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas para análise:', col_analises_filtradas)

valor_selecionado = st.sidebar.selectbox('Selecione a análise:', COLUNAS_VALOR)

metrica_selecionada = st.sidebar.selectbox('Selecione a métrica:', list(FUNCOES_AGG.keys()))

if len(indices_selecionados) > 0 and len(colunas_selecionadas) > 0:
    metrica_selecionada = FUNCOES_AGG[metrica_selecionada]
    vendas_pivotadas = pd.pivot_table(df_vendas, 
                                      index=indices_selecionados, 
                                      columns=colunas_selecionadas, 
                                      values=valor_selecionado, 
                                      aggfunc=metrica_selecionada
                                      )
    vendas_pivotadas['TOTAL GERAL'] = vendas_pivotadas.sum(axis=1)
    vendas_pivotadas.loc['TOTAL GERAL'] = vendas_pivotadas.sum(axis=0).to_list()
    st.dataframe(vendas_pivotadas) 

