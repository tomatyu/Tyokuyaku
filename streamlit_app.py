import streamlit as st
import pydeck as pdk

# Streamlitのタイトル
st.title('回転可能な3Dビジュアライゼーション')

# pydeckの3Dビジュアライゼーションを作成
deck = pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=0,  # 緯度
        longitude=0,  # 経度
        zoom=1,  # ズームレベル
        pitch=45,  # 傾き（地球儀風に見せるための角度）
        bearing=0  # 回転
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=[
                {'position': [-122.4194, 37.7749], 'size': 100},  # サンフランシスコの座標
                {'position': [139.6917, 35.6895], 'size': 100},  # 東京の座標
            ],
            get_position='position',
            get_fill_color=[255, 0, 0],
            get_radius='size',
            radius_scale=10,
            radius_min_pixels=5
        )
    ],
    # 地球儀に近い3Dビューを提供するための設定
    views=[pdk.view.OrbitalView()],
    tooltip={"text": "{position}"}
)

# Streamlitで3Dビジュアライゼーションを表示
st.pydeck_chart(deck)
