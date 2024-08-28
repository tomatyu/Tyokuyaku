import streamlit as st
from janome.tokenizer import Tokenizer
import pandas as pd

# 関数: データの読み込み
def load_data():
    try:
        return pd.read_excel("56.xlsx")  # Excelファイルのパスと拡張子を確認してください
    except Exception as e:
        st.error(f"ファイルの読み込みに失敗しました: {e}")
        return pd.DataFrame()  # 空のデータフレームを返す

# 初期設定
st.title('古文ツール')

# サイドバーで機能の選択
option = st.sidebar.selectbox('選択してください', ['文節分割ツール', '直訳検索ツール'])

# 文節分割ツール
if option == '文節分割ツール':
    st.header('古文の文節分割ツール')
    
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

# 直訳検索ツール
elif option == '直訳検索ツール':
    st.header('古文直訳ツール')
    
    # データの読み込み
    countries_df = load_data()
    
    # サイドバーでの単語入力
    st.sidebar.header("単語入力")
    inputs = [st.sidebar.text_input(f"単語 {i+1}", key=f"input_{i}") for i in range(60)]
    
    st.write("上から文節ごとに:red[ひらがなで]入力してください。（最大60単語適応）")
    
    # 「直訳を表示」ボタンがクリックされたときの処理
    if st.button('直訳を表示'):
        meanings = []
        for word in inputs:
            if word.strip() != "":  # 空でない単語のみ検索
                kv = countries_df[countries_df["古文"] == word]
                if not kv.empty:
                    meanings.append(kv["意味"].iloc[0])
                else:
                    meanings.append(f"'{word}' の検索結果が見つかりませんでした")
            else:
                meanings.append("")
        
        # 検索結果を表示
        st.write(" ".join(meanings))
