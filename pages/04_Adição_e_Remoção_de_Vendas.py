import streamlit as st
from pathlib import Path
import pandas as pd
from utilidades import leitura_dados

#Sidebar
st.sidebar.markdown('Desenvolvido por [Orenjy](https://orenjy.com/)')

leitura_dados()

df_vendas = st.session_state['dados']['vendas']
df_filiais = st.session_state['dados']['filiais']
df_produtos = st.session_state['dados']['produtos']

st.dataframe(df_vendas)
st.dataframe(df_filiais)
st.dataframe(df_produtos)