import streamlit as st
import pandas as pd

def df_change(df,data):
    df= pd.DataFrame(data=data)
    df
    return 

data = [10, 100 ,100]
data2 = [100,100,100]

df = pd.DataFrame(data=data)
st.write('hi')
result = st.button('click')

if result:
    st.write(result)


st.area_chart(data=data)

df




