import streamlit as st
from pathlib import Path
import pandas as pd
from utilidades import leitura_dados

# Logotipo
st.logo(
    Path(__file__).parents[1] / 'identidade_visual' / 'logo_completo.png',
    size='large',
    link = 'https://orenjy.com/',
    icon_image=Path(__file__).parents[1] / 'identidade_visual' / 'logo_pequeno.png',
)

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
    col1, col2 = st.sidebar.columns(2)
    filtro_selecionado = col1.selectbox('Selecione o filtro:', 
                     list(df_vendas.columns))
    valores_unicos_coluna = list(df_vendas[filtro_selecionado].unique())
    valor_filtro = col2.selectbox('Selecione o valor:',
                                  valores_unicos_coluna)
    filtrar = col1.button('Filtrar')
    limpar = col2.button('Limpar')

    if filtrar:
        st.dataframe(df_vendas.loc[df_vendas[filtro_selecionado] == valor_filtro, colunas_selecionadas], height=800, width=1000)
    elif limpar:
        st.dataframe(df_vendas[colunas_selecionadas], height=800, width=1000)
    else:
        st.dataframe(df_vendas[colunas_selecionadas], height=800, width=1000)


if tabela_selecionada == 'Produtos':
    mostra_tabela_produtos()
elif tabela_selecionada == 'Filiais':
    mostra_tabela_filiais()
elif tabela_selecionada == 'Vendas':
    mostra_tabela_vendas()