import streamlit as st
import pandas as pd

# 世界遺産の位置情報
world_heritage_data = pd.DataFrame({
    '名前': ['キリマンジャロ', 'エーゲ海の島々', 'クスコ歴史地区', 'タージ・マハル', 'グランドキャニオン国立公園', 'メキシコシティ歴史地区', 'クスコ歴史地区', 'モンテ・サン・ミシェル', 'シルクロード', 'イエローストーン国立公園'],
    'lat': [38.5342],
    'lot': [77.0212]
})

def main():
    st.title("世界遺産地図")

    # 地図上に世界遺産のピンを表示
    st.map(world_heritage_data)

if __name__ == "__main__":
    main()