import streamlit as st
import pydeck as pdk

# Streamlitのタイトル
st.title('回転可能な地球儀風のビジュアライゼーション')

# pydeckの地球儀風のビジュアライゼーションを作成
deck = pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=0,  # 緯度
        longitude=0,  # 経度
        zoom=1,  # ズームレベル
        pitch=30,  # 傾き
        bearing=0  # 回転
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=[
                {'position': [-122.4194, 37.7749], 'size': 100},  # サンフランシスコ
                {'position': [139.6917, 35.6895], 'size': 100},  # 東京
            ],
            get_position='position',
            get_fill_color=[255, 0, 0],
            get_radius='size',
            radius_scale=10,
            radius_min_pixels=5
        )
    ],
    views=[pdk.view.GlobeView()],
    tooltip={"text": "{position}"}
)

# Streamlitで地球儀風のビジュアライゼーションを表示
st.pydeck_chart(deck)
