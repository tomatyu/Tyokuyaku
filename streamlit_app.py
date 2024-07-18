import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import numbers

a = st.numbers_input("")
b = st.numbers_input("")
c = st.numbers_input("")
d = st.numbers_input("")
e = st.numbers_input("")

kazu = [a,b,c,d,e]
subject = ["国語","英語","数学","理科","社会"]
fig = go.Figure(data=[go.Bar(x=subject, y=kazu)])

fig.update_layout(
    xaxis = dict(
        tickangle = 0,
        title_text = "教科",
        title_font = {"size": 20},
        title_standoff = 25),
    yaxis = dict(
        title_text = "点数",
        title_standoff = 25),
    title ='Title')

st.title("テスト表示")

if st.button("表示"):
    st.plotly_chart(fig, use_container_width=True)
