import streamlit as st
import pandas as pd
import plotly as px

st.title("テスト表示")
a = st.text_input("国語")
b = st.text_input("英語")
c = st.text_input("数学")
d = st.text_input("理科")
e = st.text_input("社会")
gdp_data = {
    "教科":["国語","英語","数学","理科","社会"],
    "点数":[a,b,c,d,e]
}
if st.button("点数を表示する"):
    counter = px.bar(gdp_data,x="教科",y="点数")
    st.plotly_chart(counter)
