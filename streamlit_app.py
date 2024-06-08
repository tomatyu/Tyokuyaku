import streamlit as st
import pandas as pd
import numpy as np

# 世界遺産の位置情報
a = pd.DataFrame({'lat': [38.5342],'lot': [77.0212]})

def main():
    st.title("世界遺産地図")

    # 地図上に世界遺産のピンを表示
st.map(a)