import streamlit as st
import pandas as pd


if 'increase_count' not in st.session_state:
    st.session_state['increase_count']=0

def inc_session():
    st.session_state['increase_count']+=1
    

def dec_session():
    if st.session_state['increase_count'] > 0:
        st.session_state['increase_count'] -= 1
    else:
        return
 

result = st.button('click',key='clearbutton',on_click=inc_session)
modify = st.button('수정',on_click=dec_session)

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





