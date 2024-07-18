import streamlit as st
import pandas as pd
import plotly as px
import numpy as np

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
  chart_data = pd.DataFrame(
   {
       "col1": "教科",
       "col2": "点数",
   }
)
  st.bar_chart(chart_data, x="col1", y="col2", color="col3")