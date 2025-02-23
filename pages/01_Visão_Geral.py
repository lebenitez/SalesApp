import streamlit as st
from pathlib import Path
import pandas as pd
from utilidades import leitura_dados, COMISSAO
from datetime import date, timedelta
import plotly.express as px

selecao_keys = {'Filial': 'filial', 
                'Vendedor': 'vendedor', 
                'Produto': 'produto',
                'Forma de Pagamento': 'forma_pagamento',
                'Gênero': 'genero'}

# Logotipo
st.logo(
    Path(__file__).parents[1] / 'identidade_visual' / 'logo_completo.png',
    size='large',
    link = 'https://orenjy.com/',
    icon_image=Path(__file__).parents[1] / 'identidade_visual' / 'logo_pequeno.png',
)

#Sidebar
st.sidebar.markdown('Desenvolvido por [Orenjy](https://orenjy.com/)')

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

data_final_default = df_vendas.index.date.max()
data_inicial_default = date(year=data_final_default.year, month=data_final_default.month, day=1)

data_inicial = st.sidebar.date_input('Data Inicial',
                          data_inicial_default
                          )

data_final = st.sidebar.date_input('Data Final',
                          data_final_default
                          )

analise_selecionada = st.sidebar.selectbox('Análise:',
                                           selecao_keys.keys()
)

analise_selecionada = selecao_keys[analise_selecionada]


df_vendas_corte = df_vendas[(df_vendas.index.date >= data_inicial) & (df_vendas.index.date <= data_final)]
df_vendas_anterior = df_vendas[(df_vendas.index.date >= data_inicial - timedelta(days=30)) & (df_vendas.index.date <= data_final - timedelta(days=30))]

st.markdown('## Dashboard de Vendas')

col1, col2, col3, col4 = st.columns(4)

valor_vendas = f"R$ {df_vendas_corte['preco'].sum():,.2f}"
dif_metrica = df_vendas_corte['preco'].sum() - df_vendas_anterior['preco'].sum()
col1.metric('Valor de Vendas', 
            valor_vendas,
            float(dif_metrica))

quantidade_vendas = df_vendas_corte['preco'].count()
dif_metrica = df_vendas_corte['preco'].count() - df_vendas_anterior['preco'].count()
col2.metric('Quantidade de Vendas', 
            quantidade_vendas,
            int(dif_metrica))

principal_filial = df_vendas_corte['filial'].value_counts().index[0]

col3.metric('Principal Filial',
            principal_filial,
)


principal_vendedor = df_vendas_corte['vendedor'].value_counts().index[0]

col4.metric('Principal Vendedor',
            principal_vendedor,
)

st.divider()

col21, col22 = st.columns(2)

df_vendas_corte['dia_venda'] = df_vendas_corte.index.date
venda_dia = df_vendas_corte.groupby('dia_venda')['preco'].sum()
venda_dia.name = 'Valor de Vendas'

fig = px.line(venda_dia, title='Vendas Diárias')
col21.plotly_chart(fig)

fig = px.pie(df_vendas_corte, 
             names=analise_selecionada,
             values='preco'
)
col22.plotly_chart(fig)

st.divider()