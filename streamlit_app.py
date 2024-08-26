import streamlit as st
import pydeck as pdk

# Streamlitのタイトル
st.title('地球儀の表示')

# pydeckの地球儀を作成
deck = pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=37.7749,  # 緯度（例: サンフランシスコ）
        longitude=-122.4194,  # 経度（例: サンフランシスコ）
        zoom=5,  # ズームレベル
        pitch=30  # 傾き
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=[
                {'position': [-122.4194, 37.7749]}  # サンプルデータ
            ],
            get_position='position',
            radius=1000,
            extruded=True,
            coverage=1
        )
    ],
    tooltip={"text": "{position}"}
)

# Streamlitで地球儀を表示
st.pydeck_chart(deck)
