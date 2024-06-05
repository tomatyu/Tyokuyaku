import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    columns=['lat', 'lon'])
st.tittle("世界歴史検索")
st.map(df)