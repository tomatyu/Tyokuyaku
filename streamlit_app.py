import streamlit as st
from janome.tokenizer import Tokenizer

# 初期設定
st.title('古文の文節分割ツール')

# 入力ボックス
text_input = st.text_area('古文テキストを入力してください', height=200)

# 文節分割処理
if text_input:
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text_input)
    
    # 文節ごとに分割
    segments = [token.surface for token in tokens]

    # 結果の表示
    st.subheader('文節ごとに分割した結果')
    st.write('/ '.join(segments))
