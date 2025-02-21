import streamlit as st
from pathlib import Path
import pandas as pd
from utilidades import leitura_dados


leitura_dados()
df_vendas = st.session_state['dados']['vendas']
df_filiais = st.session_state['dados']['filiais']
df_produtos = st.session_state['dados']['produtos']


#Sidebar
st.sidebar.markdown('## Tabelas')
tabela_selecionada = st.sidebar.selectbox('Selecione a tabela:', 
                     ['Vendas', 
                      'Filiais', 
                      'Produtos'
                      ])

def mostra_tabela_produtos():
    st.dataframe(df_produtos)

def mostra_tabela_filiais():
    st.dataframe(df_filiais)

def mostra_tabela_vendas():
    st.sidebar.divider()
    st.sidebar.markdown('### Filtrar tabela')
    colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas:', 
                                          list(df_vendas.columns),
                                          list(df_vendas.columns)
                                          )
    st.dataframe(df_vendas[colunas_selecionadas])



if tabela_selecionada == 'Produtos':
    mostra_tabela_produtos()
elif tabela_selecionada == 'Filiais':
    mostra_tabela_filiais()
elif tabela_selecionada == 'Vendas':
    mostra_tabela_vendas()