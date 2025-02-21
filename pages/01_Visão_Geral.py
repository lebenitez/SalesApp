import streamlit as st
from pathlib import Path
import pandas as pd
from utilidades import leitura_dados

#Sidebar
st.sidebar.markdown('Desenvolvido por [Orenjy](https://orenjy.com/)')

leitura_dados()