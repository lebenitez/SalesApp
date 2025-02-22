import streamlit as st
from pathlib import Path

# Logotipo
st.logo(
    Path(__file__).parent / 'identidade_visual' / 'logo_completo.png',
    size='large',
    link = 'https://orenjy.com/',
    icon_image=Path(__file__).parent / 'identidade_visual' / 'logo_pequeno.png',
)

#Sidebar
st.sidebar.markdown('Desenvolvido por [Orenjy](https://orenjy.com/)')

# Corpo da página
st.markdown('# Bem-vindo ao Sistema de Vendas')
st.divider()

st.markdown(
    '''
    ### O que é o Sistema de Vendas?
    O Sistema de Vendas é um projeto ***open-source*** que visa ajudar pequenos comerciantes a gerenciar suas vendas.
    Com ele, é possível cadastrar produtos, clientes, fornecedores e realizar vendas.
    '''
)


 