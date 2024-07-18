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
major_countries = [gdp_data]
comparison_data = [major_countries]

if st.button("点数を表示する"):
    comparison_data = [major_countries]
    fig_comparison = comparison_data, x = 教科, y = 点数, color = 教科,
    labels={'点数': '点数', "教科": "教科"}
    st.plotly_chart(fig_comparison)