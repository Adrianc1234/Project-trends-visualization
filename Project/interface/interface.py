import streamlit.components.v1 as components
import pandas as pd
import streamlit as st
import numpy as np

username = st.text_input('User Name: ', '@example')

#boton scrapping
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #212F3C;
    color:#00ff00;
}
div.stButton > button:hover{
    background-color: #148F77 ;
    color:#F8F9F9;
    }
</style>""", unsafe_allow_html=True)

#LIMPIEZA DE USUARIO
def remove_arr(username):
    text = username[1::]
    return text

#BOTON DE BUSQUEDA
if st.button('Lets do it!') and username == "@example":
    st.write(f'This user name is not valid!')

elif username == "@example":
    st.write(f'please enter your username!')

elif len(username) == 0 or '@' not in username:
    st.write(f'This user name is not valid!')

else:
    st.write(f'Username {username} was gotten successfully!')
    username = remove_arr(username)






