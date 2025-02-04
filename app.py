import streamlit as st

import streamlit as st

st.markdown("""
<style>
    body {
        background-color: #ffffff; 
        color: #000000; 
    }
    .stSidebar {
        background-color: #2e6ed5; 
    }
    .stSidebar [data-testid="stMarkdownContainer"] p {
        color: #ffffff; 
    }
</style>
""", unsafe_allow_html=True)

def main() :

    st.title('경기도 경기부동산')
    menu=['Home','분양권 실거래가','업무/사업용 실거래가','오피스텔 실거래가']
    choice=st.sidebar.selectbox('Menu',menu)

    if choice==menu[0] :
        pass
    elif choice==menu[1] :
        pass
    elif choice==menu[2] :
        pass
    elif choice==menu[3] :
        pass

if __name__=='__main__' :
    main()