import streamlit as st
from PIL import Image
import os
import pandas as pd

st.markdown("<h1 style='text-align: center;'>자료수집 방법 결정</h1>", unsafe_allow_html=True)
st.divider()

st.markdown("<h4 style='text-align: left;'>1. 직접 설문하기</h4>", unsafe_allow_html=True)
st.write("  **(구글 설문지, 통그라미, 네이버 설문 등)**")
st.markdown("<h4 style='text-align: left;'>2. 직접 실험하기</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: left;'>3. 기존 온라인자료 이용하기(통계청, 공공데이터)</h4>", unsafe_allow_html=True)
st.write("  **+ 사전조사, 인터뷰, 현장조사, 후속조사 등**")
st.write("**:ballot_box_with_check: 계획 수립 및 역할 분담**")

st.divider()

st.selectbox(":bookmark_tabs: **결정한 자료수집 방법은 무엇인가요?**",['직접 설문하기','직접 실험하기','온라인자료 이용하기'], placeholder="Choose an option")

con1, con2= st.columns([0.4,0.6])
with con1:
    st.text_input(':link: **설문하기를 선택했다면 설문 링크를 올려주세요**')
with con2: 
    uploaded_file = st.file_uploader(":file_folder: **온라인자료 이용을 선택했다면 데이터 파일을 올려주세요.**", type=['csv'])

    if uploaded_file is not None:
        try:
            if uploaded_file.type == 'application/vnd.ms-excel':
                data1 = pd.read_excel(uploaded_file)
            else:
                data1 = pd.read_csv(uploaded_file,encoding='cp949')
        except Exception as e:
            st.write("There was an error in loading the file.")
            st.write(e)
