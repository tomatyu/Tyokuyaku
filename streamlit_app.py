import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import numpy as np
import numbers

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
# 多角形を閉じるためにデータの最後に最初の値を追加する。
radar_values = np.concatenate([kazu, [kazu[0]]])
# プロットする角度を生成する。
angles = np.linspace(0, 2 * np.pi, len(subject) + 1, endpoint=True)

kig = plt.figure(facecolor="w")
# 極座標でaxを作成。
ax = kig.add_subplot(1, 1, 1, polar=True)
# レーダーチャートの線を引く
ax.plot(angles, radar_values)
#　レーダーチャートの内側を塗りつぶす
ax.fill(angles, radar_values, alpha=0.2)
# 項目ラベルの表示
ax.set_thetagrids(angles[:-1] * 180 / np.pi, subject)

ax.set_title("レーダーチャート", pad=20)
plt.show()


st.title("テスト表示")

if st.button("表示"):
    st.plotly_chart(fig, use_container_width=True)
    st.line_chart(kig, use_container_width=True)
  