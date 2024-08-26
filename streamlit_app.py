import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Streamlitのタイトル
st.title('立体の球体の表示')

# 球体のデータ生成
def generate_sphere():
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

x, y, z = generate_sphere()

# Plotlyの球体を作成
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis')])
fig.update_layout(scene=dict(
                    xaxis=dict(nticks=4, range=[-0.05, 0.05]),
                    yaxis=dict(nticks=4, range=[-0.05, 0.05]),
                    zaxis=dict(nticks=4, range=[-0.05, 0.05]),
                    aspectratio=dict(x=1, y=1, z=1)
                  ))

# Streamlitで球体を表示
st.plotly_chart(fig)
