import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import numbers

a = st.number_input("国語",value=10)
b = st.number_input("英語",value=10)
c = st.number_input("数学",value=10)
d = st.number_input("理科",value=10)
e = st.number_input("社会",value=10)

kazu = [a,b,c,d,e]
subject = ["国語","英語","数学","理科","社会"]
fig = go.Figure(data=[go.Bar(x=subject, y=kazu)])

fig.update_layout(
    xaxis = dict(
        tickangle = 0,
        title_text = "教科",
        title_font = {"size": 10},
        title_standoff = 15),
    yaxis = dict(
        title_text = "点数",
        title_standoff = 25),
    title ='Title')

st.title("テスト表示")

if st.button("表示"):
    st.plotly_chart(fig, use_container_width=True)
