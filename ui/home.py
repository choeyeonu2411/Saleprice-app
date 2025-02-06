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
    
    image = Image.open('img/menu.jpg')
    st.image(image, use_container_width=True)

    st.markdown("<hr style='border: 1px solid #3366cc; margin: 20px 0;'>", unsafe_allow_html=True)

    # CSS 스타일 정의
    st.markdown("""
    <style>
        .header {
            font-size: 24px;
            font-weight: bold;
            color: #3366cc;
            text-align: center;
            padding: 20px 0;
            margin-bottom: 20px;
            border-bottom: 2px solid #3366cc;
        }
        .feature-box {
            background-color: #f0f8ff;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            height: 150px; /* 고정 높이 설정 */
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .feature-icon {
            font-size: 24px;
            margin-bottom: 10px;
        }
        .feature-title {
            font-size: 18px;
            font-weight: bold;
            color: #3366cc;
            margin-bottom: 5px;
        }
        .feature-desc {
            font-size: 14px;
            color: #666;
        }
        .metric-box {
            background-color: #e6f2ff;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            height: 150px; /* 고정 높이 설정 */
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .metric-value {
            font-size: 24px;
            font-weight: bold;
            color: #3366cc;
        }
        .metric-label {
            font-size: 16px;
            color: #666;
            margin-top: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

    # 나머지 코드는 이전과 동일


    # 첫 번째 섹션: 주요 기능
    st.markdown("<div class='header'>주요 기능</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='feature-box'>
            <div class='feature-icon'>🔍</div>
            <div class='feature-title'>지역별 실거래가 조회</div>
            <div class='feature-desc'>경기도 전역의 상세 실거래가 정보</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature-box'>
            <div class='feature-icon'>📊</div>
            <div class='feature-title'>AI 가격 예측</div>
            <div class='feature-desc'>머신러닝 기반 정확한 가격 예측</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='feature-box'>
            <div class='feature-icon'>📈</div>
            <div class='feature-title'>시장 동향 분석</div>
            <div class='feature-desc'>최신 부동산 시장 트렌드 제공</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # 두 번째 섹션: 서비스 현황
    st.markdown("<div class='header'>서비스 현황</div>", unsafe_allow_html=True)
    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <div class='metric-box'>
            <div class='metric-value'>10,000+</div>
            <div class='metric-label'>총 데이터 건수</div>
            <div class='feature-desc'>분석된 부동산 거래 데이터</div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class='metric-box'>
            <div class='metric-value'>31</div>
            <div class='metric-label'>분석 지역</div>
            <div class='feature-desc'>경기도 전체 시/군 포함</div>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div class='metric-box'>
            <div class='metric-value'>85%</div>
            <div class='metric-label'>예측 정확도</div>
            <div class='feature-desc'>지속적인 모델 개선 중</div>
        </div>
        """, unsafe_allow_html=True)


    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; '>사용 방법</h3>",unsafe_allow_html=True)
    st.write("""
    1. 사이드바에서 원하는 메뉴를 선택하세요
    2. 지역과 동을 선택하세요
    3. 필요한 정보를 입력하세요
    4. AI 예측 결과를 확인하세요
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <h6 syle='text-align: center;'> *본 서비스의 예측 결과는 참고용이며, 실제 거래 시 전문가와 상담을 권장합니다.*</h>
    """,unsafe_allow_html=True)
        

