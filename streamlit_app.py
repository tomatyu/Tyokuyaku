import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Streamlitのタイトル
st.title('大きな立体の球体の表示')

# 球体のデータ生成
def generate_sphere(radius=1):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

# 半径を指定して球体を生成
radius = 2  # 球体の半径
x, y, z = generate_sphere(radius)

# Plotlyの球体を作成
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis')])
fig.update_layout(
    scene=dict(
        xaxis=dict(nticks=4, range=[-radius-0.5, radius+0.5]),
        yaxis=dict(nticks=4, range=[-radius-0.5, radius+0.5]),
        zaxis=dict(nticks=4, range=[-radius-0.5, radius+0.5]),
        aspectratio=dict(x=1, y=1, z=1)
    ),
    title='大きな立体の球体'
)

# Streamlitで球体を表示
st.plotly_chart(fig)
