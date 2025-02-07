from PIL import Image
import streamlit as st

from ui.eda import run_eda
from ui.affairs import run_affairs
from ui.home import run_home
from ui.officetel import run_office
from ui.sale import run_sale


def main() :

    st.markdown("<h1 style='text-align: center; color: black;'> 경기도 경기부동산 실거래가 예측 APP</h1>", unsafe_allow_html=True)
    menu=['Home','데이터 분석','🏠 아파트 실거래가','🏦 업무/사업용 실거래가','🏢 오피스텔 실거래가']

    # 사이드 바
    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #e6f2ff;
        }
    </style>
    """, unsafe_allow_html=True)


    with st.sidebar:

        image = Image.open('img/menu2.png')
        st.image(image, use_container_width=True)

        st.subheader('실거래가 예측 App')
        
        choice = st.radio("메뉴 ", menu)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <h6 syle='text-align: center;'> *본 서비스의 예측 결과는 참고용이며, 실제 거래 시 전문가와 상담을 권장합니다.*</h>
        """,unsafe_allow_html=True)


    if choice==menu[0] :
        run_home()
    elif choice==menu[1] :
        run_eda()
    elif choice==menu[2] :
        run_sale()
    elif choice==menu[3] :
        run_affairs()
    elif choice==menu[4] :
        run_office()

if __name__=='__main__' :
    main()