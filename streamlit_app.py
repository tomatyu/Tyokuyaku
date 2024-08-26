import streamlit as st
import pydeck as pdk

# Streamlitのタイトル
st.title('3D球体地球儀の表示')

# pydeckの地球儀を作成
deck = pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=0,  # 緯度
        longitude=0,  # 経度
        zoom=1,  # ズームレベル
        pitch=0  # 傾き
    ),
    layers=[
        pdk.Layer(
            'GlobeLayer',
            data=[{}],  # データは空でも球体の表示には影響なし
            get_position='[longitude, latitude]',
            radius=1,
            extruded=True
        )
    ],
    views=[pdk.view.GlobeView()]  # GlobeViewを使って球体表示
)

# Streamlitで地球儀を表示
st.pydeck_chart(deck)
