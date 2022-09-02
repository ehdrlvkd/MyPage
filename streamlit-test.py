from distutils.command.upload import upload
import streamlit as st
import pandas as pd
from io import StringIO
import sys
import time
import matplotlib


if 'increase_count' not in st.session_state:
    st.session_state['increase_count']=0

def inc_session():
    st.session_state['increase_count']=1
    

def dec_session():
    if st.session_state['increase_count'] > 0:
        st.session_state['increase_count'] = 0
    else:
        return
 

result = st.button('필터',key='clearbutton',on_click=inc_session)
modify = st.button('초기화',on_click=dec_session)

if result:
    if st.session_state['clearbutton']:
        st.session_state
        "hi"
    else :
        "bye"

if modify:
    if st.session_state['clearbutton']==False:
        st.session_state
        "bye"


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
    st.write(uploaded_file.name)
    df2 = pd.read_csv(uploaded_file,encoding="cp949")
    
    headers = []
    for col in df2.columns:
        headers.append(col)

    st.write(headers)
    if st.session_state['increase_count'] == 1:
        data_filter = df2[df2['주소'].str.contains("개포동")]
        st.write(df2['구정보'].value_counts())
        # st.write(df2[df2['주소'].str.contains("개포동")].describe(include='all'))
    else:
        st.write(df2)



# df = pd.read_csv('data.csv',encoding="cp949")

# st.write(df)