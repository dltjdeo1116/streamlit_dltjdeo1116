import streamlit as st
from PIL import Image
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.markdown("<h1 style='text-align: center;'>데이터 수집과 분석</h1>", unsafe_allow_html=True)
st.divider()

st.markdown("<h3 style='text-align: left;'>자료의 종류</h3>", unsafe_allow_html=True)
st.image('images/image00.png')

st.markdown("<h3 style='text-align: left;'>목적에 맞는 데이터 시각화 차트 유형</h3>", unsafe_allow_html=True)


with st.expander("**:blue[[비교]]**"):
    st.write("**막대차트(Bar Chart), 그룹막대차트(Paired Bar), 버블차트(Bubble Chart)**")
    st.image('images/image01.png')


with st.expander("**:blue[[추이]]**"):
    st.write("**선차트 (Line Chart), 영역차트(Area Chart), 타임라인차트(Timeline chart)**")
    st.image('images/image02.png')

        
with st.expander("**:blue[[비율]]**"):
    st.write("**파이차트(Pie Chart), 와플차트(Waffle Chart), 트리맵(Treemap)**")
    st.image('images/image03.png')
    st.image('images/image03_1.png')
    


with st.expander("**:blue[[관계]]**"):
    st.write("**산점도(Scatter Plot), 네트워크 시각화, XY 히트맵(XY Heat map)**")
    st.image('images/image04.png')
   

with st.expander("**:blue[[위치]]**"):
    st.write("**필드맵(Field Map), 기호맵(Symbol Map), 흐름도(Flow Map)**")
    st.image('images/image05.png')
    
st.divider()

st.markdown("<h3 style='text-align: left;'>예시 데이터를 이용한 그래프 그리기</h3>", unsafe_allow_html=True)

def main():
    df = pd.read_csv('data/학교급 및 시도별 학생 1인당 월평균 사교육비.csv', encoding='cp949')
    st.dataframe(df)

title = st.selectbox("**데이터 선택**", ['학교급 및 시도별 학생 1인당 월 사교육비','우리나라 10대 수출품목별 금액', '본인이 업로드한 데이터'], placeholder="Choose an option")
if title == '학교급 및 시도별 학생 1인당 월 사교육비' :
    hold=st.selectbox("**고정할 것**",['연도','학교급', '시도'], placeholder="Choose an option")
    x=st.selectbox("**x축**",['연도','학교급', '시도'], placeholder="Choose an option")
if title == '우리나라 10대 수출품목별 금액' :
    hold=st.selectbox("**고정할 것**",['연도', '품목순위'], placeholder="Choose an option")
    x=st.selectbox("**x축**",['연도', '품목순위'], placeholder="Choose an option")
if title == '본인이 업로드한 데이터' :
    x = st.text_input(':bar_chart: **x축**')
    y = st.text_input(':bar_chart: **y축**')


st.divider()

method = st.text_area(':pencil: **진행했던 탐구방법과 문제해결 과정을 정리해보세요**', key="method_text_area")
Result = st.text_area(':pencil: **새롭게 알게된 사실이나 결과를 적어보세요**', key="result_text_area")
Conclusion = st.text_area(':pencil: **결론 및 문제해결을 위한 제안**', key="conclusion_text_area")
