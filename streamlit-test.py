from turtle import onclick
import streamlit as st
import pandas as pd


data = [10, 100 ,100]
data2 = [100,100,100]

df = pd.DataFrame(data=data)
st.write('hi')
result = st.button('click')

if result:
    data = data2
    st.write(result)
    st.area_chart(data=data)
    st.write(data)
    st.write(data2)
else:
    st.area_chart(data=data)




df




