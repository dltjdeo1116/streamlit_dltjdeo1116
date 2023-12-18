import streamlit as st
from PIL import Image
import os

st.markdown("<h1 style='text-align: center;'>통계포스터 제작</h1>", unsafe_allow_html=True)
st.divider()

st.markdown("<h4 style='text-align: left;'>1. 조별로 통계포스터 제작하며 모은 자료들을 정리한다.</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: left;'>2. Canva사이트를 이용해 보고서 제작하기</h4>", unsafe_allow_html=True)
st.link_button("Canva 링크", "https://www.canva.com/ko_kr/")
st.write("**(Streamlit 사이트에서 정리한 글들은 복사, 그래프는 캡처해서 이용)**")
uploaded_file = st.file_uploader("완성된 통계포스터 이미지 사진으로 첨부", type=["jpg", "png", "jpeg", "gif", "bmp"], accept_multiple_files=True)

st.divider()

st.subheader(":smile: 어렵지만 재밌었나요?")
st.subheader("배운것을 활용해서 통계활용대회를 나가봅시다!")