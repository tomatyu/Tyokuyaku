import streamlit as st
import pydeck as pdk

# Streamlitのタイトル
st.title('地球儀風のデータ表示')

# pydeckの地球儀風のビジュアライゼーションを作成
deck = pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=0,  # 緯度
        longitude=0,  # 経度
        zoom=1,  # ズームレベル
        pitch=50  # 傾き
    ),
    layers=[
        pdk.Layer(
            'ArcLayer',
            data=[
                {
                    'start': [-122.4194, 37.7749],  # サンフランシスコの座標
                    'end': [139.6917, 35.6895],  # 東京の座標
                }
            ],
            get_source_position='start',
            get_target_position='end',
            get_source_color=[255, 0, 0],
            get_target_color=[0, 0, 255],
            radius=1000,
            width_scale=10
        )
    ]
)

# Streamlitで地球儀風のビジュアライゼーションを表示
st.pydeck_chart(deck)
