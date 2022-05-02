import streamlit as st 
import pandas as pd
import numpy as np

st.set_page_config(page_title = 'SDG Dashboard', 
    layout='wide',
    page_icon='')

### top row 

hunger = pd.read_csv("./hunger-data.csv")
test = hunger.T["World"][5]
# test = 8.9
hunger

st.markdown("## UN SDG")

first_kpi, second_kpi= st.columns(2)


with first_kpi:
    st.markdown("**Zero hunger**")
    number1 = test 
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)
    st.markdown("*Measured by Undernourishment")

with second_kpi:
    st.markdown("**Poverty**")
    number2 = test 
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)


st.markdown("## Chart Section: 1")

first_chart, second_chart = st.columns(2)


with first_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with second_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)


st.markdown("## Chart Section: 2")

first_chart, second_chart = st.columns(2)


with first_chart:
    chart_data = pd.DataFrame(np.random.randn(100, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with second_chart:
    chart_data = pd.DataFrame(np.random.randn(2000, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
