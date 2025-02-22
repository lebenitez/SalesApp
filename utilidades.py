import streamlit as st
from pathlib import Path
import pandas as pd

def leitura_dados():
    if not 'dados' in st.session_state:
        pasta_datasets = Path(__file__).parent / 'datasets'
        df_vendas = pd.read_csv(pasta_datasets / 'vendas.csv', decimal=',', sep=';', index_col=0,parse_dates=True)
        df_filiais = pd.read_csv(pasta_datasets / 'filiais.csv', sep=';', index_col=0)
        df_produtos = pd.read_csv(pasta_datasets / 'produtos.csv', sep=';', index_col=0)
        dados = {'vendas': df_vendas, 
                'filiais': df_filiais, 
                'produtos': df_produtos}
        st.session_state['caminho_datasets'] = pasta_datasets
        st.session_state['dados'] = dados