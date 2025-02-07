
import pandas as pd
import streamlit as st
from PIL import Image

def run_home() :
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; color: gray;'>- AI 기반 부동산 실거래가 예측 서비스 -</h3>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; font-size:13px;'>
    경기도 부동산 실거래가 예측 서비스는 최신 빅데이터와 AI 기술을 활용하여<br>
    예측한 부동산 가격 정보를 제공합니다.
    </p>
    """, unsafe_allow_html=True)
    
    image = Image.open('img/home.jpg')
    st.image(image, use_container_width=True)

    st.markdown("<hr style='border: 1px solid #3366cc; margin: 20px 0;'>", unsafe_allow_html=True)


    st.markdown("""
    ## 앱 소개
    이 앱은 최신 AI 기술을 활용하여 경기도 지역의 주택 실거래가를 예측합니다. 
    다양한 요인을 고려하여 정확한 예측 결과를 제공하며, 부동산 투자 및 주택 구매 결정에 도움을 드립니다.

    ### 주요 기능
    - 지역별 주택 실거래가 예측
    - 최신 부동산 동향 분석
    - 맞춤형 투자 조언
    """)

    st.info("""
    ### 사용 방법
    1. 사이드바에서 원하는 메뉴를 선택하세요
    2. 지역과 동을 선택하세요
    3. 필요한 정보를 입력하세요
    4. AI 예측 결과를 확인하세요
    """)

    

    


    with st.expander("앱 사용 팁"):
        st.write("""
        - AI 예측 모델의 정확도: 약 85% (2024 데이터 기준)
        - 주요 고려 변수: 위치, 면적, 층수, 건축 연도, 주변 인프라 등
        - 특정 지역의 개발 계획이나 정책 변화는 별도로 고려해야 함
        """)
        

