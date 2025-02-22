import streamlit as st
from pathlib import Path
import pandas as pd
from utilidades import leitura_dados
from datetime import datetime

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
    lista_adicionar = [df_vendas['id_venda'].max() + 1,
                       filial_selecionada.split('/')[0],
                       vendedor_selecionado,
                       produto_selecionado,
                       nome_cliente,
                       genero_cliente,
                       forma_pagamento
                       ]
    hora_adicionar = datetime.now()
    df_vendas.loc[hora_adicionar] = lista_adicionar
    caminho_dataset = st.session_state['caminho_datasets']
    df_vendas.to_csv(caminho_dataset / 'vendas.csv', decimal=',', sep=';')
    st.dataframe(df_vendas)

st.sidebar.markdown('## Remoção de Vendas')
id_remocao = st.sidebar.number_input('ID da venda a ser removida:', min_value=0, max_value=df_vendas['id_venda'].max())
remover_venda = st.sidebar.button('Remover Venda')
if remover_venda:
    df_vendas = df_vendas[df_vendas['id_venda'] != id_remocao]
    caminho_dataset = st.session_state['caminho_datasets']
    df_vendas.to_csv(caminho_dataset / 'vendas.csv', decimal=',', sep=';')
    st.session_state['dados']['df_vendas'] = df_vendas
    
st.dataframe(df_vendas, height=800)


# Sidebar
st.sidebar.divider()
st.sidebar.markdown('Desenvolvido por [Orenjy](https://orenjy.com/)')