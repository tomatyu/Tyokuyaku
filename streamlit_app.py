import streamlit as st

# 初回実行時に状態を初期化
if 'count' not in st.session_state:
    st.session_state.count = 0

# ボタンが押されたときに状態を更新
if st.button('Increment'):
    st.session_state.count += 1

# 状態の表示
st.write(f'Count: {st.session_state.count}')
