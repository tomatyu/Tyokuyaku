import streamlit as st
import pandas as pd
import numpy as np

# 世界遺産の位置情報
df = pd.DataFrame({'lat': [38.5342],'lot': [77.0212]})

st.map(df)