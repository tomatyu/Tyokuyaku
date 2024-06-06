import streamlit as st
import pandas as pd

# 世界遺産の位置情報
world_heritage_data = pd.DataFrame({
    '名前': ['キリマンジャロ', 'エーゲ海の島々', 'クスコ歴史地区', 'タージ・マハル', 'グランドキャニオン国立公園', 'メキシコシティ歴史地区', 'クスコ歴史地区', 'モンテ・サン・ミシェル', 'シルクロード', 'イエローストーン国立公園'],
    'lat': [-3.0674, 37.3635, -13.5183, 27.1751, 36.1069, 19.4326, -13.1631, 48.6361, 38.8610, 44.4279],
    'lon': [37.3556, 25.2757, -71.9789, 78.0421, -112.1129, -99.1332, -72.5450, -1.5107, 66.1667, -110.5885]
})

def main():
    st.title("世界遺産地図")

    # 地図上に世界遺産のピンを表示
    selected_pin = st.map(world_heritage_data)

    # 選択されたピンの位置を取得
    selected_lat = None
    selected_lon = None
    if selected_pin is not None:
        selected_lat = selected_pin[0]['lat']
        selected_lon = selected_pin[0]['lon']

    # 選択されたピンの名前を取得
    selected_name = None
    if selected_lat is not None and selected_lon is not None:
        selected_name = world_heritage_data[(world_heritage_data['lat'] == selected_lat) & (world_heritage_data['lon'] == selected_lon)]['名前'].iloc[0]

    # 選択されたピンがあれば、その名前を表示
    if selected_name is not None:
        st.write("選択された世界遺産:", selected_name)

if __name__ == "__main__":
    main()
