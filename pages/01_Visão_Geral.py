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

#Sidebar
st.sidebar.markdown('Desenvolvido por [Orenjy](https://orenjy.com/)')

leitura_dados()