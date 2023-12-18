import streamlit as st
from PIL import Image
import os

st.markdown("<h1 style='text-align: center;'>자료선정</h1>", unsafe_allow_html=True)
st.divider()

st.markdown("<h4 style='text-align: left;'>1. 일상에서 호기심을 일었던 주제 생각하기</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: left;'>2. 사회시간에 토론했던 사회문제 참고하기</h4>", unsafe_allow_html=True)
st.write("**(생활, 학습, 과학, 환경, AI, 학교, 가정 등)**")
st.markdown("<h4 style='text-align: left;'>3. 다양한 사이트 참고하기</h4>", unsafe_allow_html=True)

tool = [
    {
        "image": r'images/image11.png',
    },
    {
        "image": r'images/image12.png',
    },    
    {
        "image": r'images/image13.png',
    },
    {
        "image": r'images/image14.png',
    },
]

for i in range(0,len(tool),2):
    row_tool = tool[i:i+2]
    cols = st.columns(2)
    
    for j in range(len(row_tool)):
        with cols[j%3]:
            current_pet = row_tool[j]
            st.image(current_pet["image"])


con1,con2, con3,con4 = st.columns([1.0,1.0,1.0,1.0])

with con1:
    st.link_button("**통그라미**", "https://tong.kostat.go.kr/front/bbs/bbsGalleryList.do?menuSn=236&bbsSn=9&menuSn=101")

with con2:
    st.link_button("**국가통계포털**", "https://kosis.kr/index/index.do")
    
with con3:
    st.link_button("**구글트렌드**", "https://trends.google.co.kr/trends/?geo=KR&hl=ko")

with con4:
    st.link_button("**data AI**", "https://www.data.ai/kr/")


st.write("**Tip. 자료 수집 용이, 흥미, 쉽고 명확한 이해와 결론 고려하기!**")

st.divider()

team_name = st.text_input(':busts_in_silhouette: **반과 조 이름을 입력해주세요.(ex. 1반 1조)**')
opinion = st.text_input(':pencil: **선정한 주제는 무엇인가요?**')
purpose = st.text_area(':pencil: **주제를 선정한 동기와 탐구 목적은 무엇인가요?**')
    
if st.button('제출'):
    if team_name is None or team_name == '':
        st.warning('반과 조 이름을 입력하세요.')
    elif opinion is None or opinion == '':
        st.warning('주제를 입력해주세요.')
    elif purpose is None or purpose == '':
        st.warning('동기나 목적을 입력해주세요.')
    else:
        st.success('자료가 제출되었습니다.')
