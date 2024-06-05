#import streamlit as st
#import pandas as pd
#import numpy as np
#df = pd.DataFrame(
    columns=['lat', 'lon'])
#st.title("世界歴史検索")
#st.map(df)
import streamlit as st
import folium

def main():
    st.title("ヨーロッパの地図")

    # ヨーロッパの中心座標
    europe_center = [51.1657, 10.4515]

    # Folium地図の作成
    m = folium.Map(location=europe_center, zoom_start=4)

    # 地図の表示
    st.write(m)

if __name__ == "__main__":
    main()
