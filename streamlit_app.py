import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as px
import numpy as np
import numbers
import requests
import json


a = st.number_input("国語",value=50,step=10,min_value=0, max_value=100)
b = st.number_input("英語",value=50,step=10,min_value=0, max_value=100)
c = st.number_input("数学",value=50,step=10,min_value=0, max_value=100)
d = st.number_input("理科",value=50,step=10,min_value=0, max_value=100)
e = st.number_input("社会",value=50,step=10,min_value=0, max_value=100)

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
df = pd.DataFrame(subject)

    # 見やすくするためにカラム名を変更、その後plotlyで読み込めるようにデータを転置
df = df.rename(columns={'f1':'国語', 'f2':'英語', 'f3':'数学', 'f4':'理科', 'f5':'社会'}).T
kig = px.line( r=df[0], theta=df.index, line_close=True, range_r=[0,1])

 


st.title("テスト表示")

if st.button("表示"):
    st.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(kig)
  