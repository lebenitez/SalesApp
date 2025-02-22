import streamlit as st
from pathlib import Path
import pandas as pd
from utilidades import leitura_dados

leitura_dados()

df_vendas = st.session_state['dados']['vendas']
df_filiais = st.session_state['dados']['filiais']
df_produtos = st.session_state['dados']['produtos']
df_filiais['cidade/estado'] = df_filiais['cidade'] + '/' + df_filiais['estado']
cidades_filiais = df_filiais['cidade/estado'].tolist()


st.sidebar.markdown('## Adição de Vendas')
filial_selecionada = st.sidebar.selectbox('Selecione a cidade da filial:', cidades_filiais)
vendedores = df_filiais.loc[df_filiais['cidade/estado'] == filial_selecionada, 'vendedores'].iloc[0]
vendedores = vendedores.strip('[]').replace("'", '').split(', ')
vendedor_selecionado = st.sidebar.selectbox('Selecione o vendedor:', vendedores)
produtos = df_produtos['nome'].tolist()
produto_selecionado = st.sidebar.selectbox('Selecione o produto:', produtos)
nome_cliente = st.sidebar.text_input('Nome do cliente:')
genero_cliente = st.sidebar.selectbox('Gênero do cliente:', ['Masculino', 'Feminino'])
forma_pagamento = st.sidebar.selectbox('Forma de pagamento:', ['Dinheiro', 'Cartão de Crédito', 'Cartão de Débito', 'Pix', 'Boleto'])
adicionar_venda = st.sidebar.button('Adicionar Venda')
if adicionar_venda:
    

st.dataframe(df_vendas)
st.dataframe(df_filiais)
st.dataframe(df_produtos)


# Sidebar
st.sidebar.divider()
st.sidebar.markdown('Desenvolvido por [Orenjy](https://orenjy.com/)')