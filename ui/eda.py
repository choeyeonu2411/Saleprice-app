from math import fma
from pkgutil import get_data
import matplotlib.pyplot as plt
import requests
import seaborn as sb
import pandas as pd
import streamlit as st

# 한글처리를 위한 코드
import numpy as np
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':  # macOS
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows':  # Windows
    font_path = r'C:\Windows\Fonts\malgun.ttf'  # 맑은 고딕
    font_prop = fma.FontProperties(fname=font_path)
    plt.rc('font', family=font_prop.get_name())
else:  # Linux
    font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  # Ubuntu의 경우
    font_prop = fm.FontProperties(fname=font_path)
    plt.rc('font', family=font_prop.get_name())


def run_eda() :

    st.subheader('탐색적 데이터 분석')
    st.info('데이터를 분석합니다.')

    df=pd.read_csv('data/주택실거래가정보.csv',encoding='cp949')
    # 뉴스 기사
    client_id = "MD8LKaxXN4pbUjfk2WBo"
    client_secret = "EV0vUZr5af"

    query = "2025 경기도 부동산 전망"
    url = f"https://openapi.naver.com/v1/search/news.json?query={query}&display=100&sort=date"

    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }

    response = requests.get(url, headers=headers)
    news_data = response.json()
    
    with st.expander("2025년 경기도 부동산 전망 기사"):
        # 뉴스 기사의 제목(20자로 제한)을 위에, 주소를 아래에 5개 출력
        for i, item in enumerate(news_data.get('items', [])):
            if i >= 5:
                break  # 5개만 출력하고 루프 종료
            title = item.get('title', '')
            title = title.replace('<b>', '').replace('</b>', '')  # HTML 태그 제거
            short_title = title[:20] + '...' if len(title) > 20 else title
            link = item.get('link', '')
            st.write(f"{short_title}")
            st.write(f"{link}")

    st.warning("주의사항: 본 앱의 예측 결과는 참고용이며, 실제 거래 시 반드시 전문가와 상담을 권장합니다.")

    st.text('2024년도 주택 실거래 데이터')
    st.dataframe(df.loc[:,['시군구명','전용면적','층','건축년도','거래금액']])

    
    # 시군구명 푱균 그래프
    # 시군구명별 평균 거래가 계산
    avg_prices = df.groupby('시군구명')['거래금액'].mean().sort_values(ascending=False)

    # 페이지 상태 초기화
    if 'page' not in st.session_state:
        st.session_state.page = 0

    # 다음/이전 페이지 함수
    def next_page():
        st.session_state.page += 1

    def prev_page():
        st.session_state.page -= 1

    # 10개씩 데이터 분할
    chunk_size = 10
    total_pages = len(avg_prices) // chunk_size + (1 if len(avg_prices) % chunk_size != 0 else 0)

    # 현재 페이지의 데이터 선택
    start = st.session_state.page * chunk_size
    end = start + chunk_size
    current_data = avg_prices.iloc[start:end]

    st.text('시군구별 평균 거래가')
    # 그래프 생성
    fig, ax = plt.subplots(figsize=(12, 6))
    current_data.plot(kind='bar', ax=ax)
    plt.title(f'페이지 {st.session_state.page + 1}/{total_pages}')
    plt.xlabel('시군구명')
    plt.ylabel('평균 거래가(만원)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Streamlit에 그래프 표시
    st.pyplot(fig)

    # 페이지 네비게이션 버튼
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.session_state.page > 0:
            st.button('이전', on_click=prev_page)

    with col3:
        if st.session_state.page < total_pages - 1:
            st.button('다음', on_click=next_page)

    with col2:
        st.write(f'페이지 {st.session_state.page + 1}/{total_pages}')


    # 통계
    with st.expander('통계 데이터 보기') :
        st.dataframe(df.loc[:,['시군구명','전용면적','층','건축년도','거래금액']].describe())


    # 상관관계 분석
    with st.expander('상관관계 분석') :
        menu=['차트로 보기','수치로 보기']
        choice=st.radio('선택하세요.',menu)
        if choice==menu[0] :
            fig1=plt.figure()
            sb.heatmap(df.loc[:,['시군구명','전용면적','층','건축년도','거래금액']].corr(numeric_only=True),annot=True, vmin=-1,vmax=1,cmap='coolwarm',linewidths=0.5)
            st.pyplot(fig1)
        elif choice==menu[1] :
            st.dataframe(df.loc[:,['시군구명','전용면적','층','건축년도','거래금액']].corr(numeric_only=True))
    