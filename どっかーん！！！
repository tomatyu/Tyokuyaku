import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px  # 修正: plotly.express を px としてインポート
import numpy as np

# 教科ごとの点数を入力
a = st.number_input("国語", value=50, step=10, min_value=0, max_value=100)
b = st.number_input("英語", value=50, step=10, min_value=0, max_value=100)
c = st.number_input("数学", value=50, step=10, min_value=0, max_value=100)
d = st.number_input("理科", value=50, step=10, min_value=0, max_value=100)
e = st.number_input("社会", value=50, step=10, min_value=0, max_value=100)

# データをリストにまとめる
kazu = [a, b, c, d, e]
subject = ["国語", "英語", "数学", "理科", "社会"]

# 棒グラフの作成（Plotly）
fig = go.Figure(data=[go.Bar(x=subject, y=kazu)])

fig.update_layout(
    xaxis=dict(
        tickangle=0,
        title_text="教科",
        title_font={"size": 15},
        title_standoff=25),
    yaxis=dict(
        title_text="点数",
        title_font={"size": 15},
        title_standoff=25),
    title='各教科の点数')

# データフレームの作成（Pandas）
df = pd.DataFrame({
    '教科': subject,
    '点数': kazu
})

# レーダーチャートの作成（Plotly Express）
kig = px.line_polar(df, r='点数', theta='教科', line_close=True)

# Streamlit アプリのタイトルと表示部分
st.title("テスト結果の表示")

if st.button("表示"):
    st.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(kig)
