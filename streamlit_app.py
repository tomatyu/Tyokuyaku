import streamlit as st
import pandas as pd
import folium

# 世界遺産の位置情報
world_heritage_data = pd.DataFrame({
    '名前': ['キリマンジャロ', 'エーゲ海の島々', 'クスコ歴史地区', 'タージ・マハル', 'グランドキャニオン国立公園', 'メキシコシティ歴史地区', 'クスコ歴史地区', 'モンテ・サン・ミシェル', 'シルクロード', 'イエローストーン国立公園'],
    'lat': [-3.0674, 37.3635, -13.5183, 27.1751, 36.1069, 19.4326, -13.1631, 48.6361, 38.8610, 44.4279],
    'lon': [37.3556, 25.2757, -71.9789, 78.0421, -112.1129, -99.1332, -72.5450, -1.5107, 66.1667, -110.5885]
})

def main():
    st.title("世界遺産地図")

    # 地図の初期位置を設定
    m = folium.Map(location=[0, 0], zoom_start=2)

    # 世界遺産のマーカーを地図に追加
    for i, row in world_heritage_data.iterrows():
        folium.Marker([row['lat'], row['lon']], popup=row['名前']).add_to(m)

    # 地図を表示
    folium_static(m)

if __name__ == "__main__":
    main()
