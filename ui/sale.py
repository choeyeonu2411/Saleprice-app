import os
import pandas as pd
import joblib 
import streamlit as st
import gdown

file_id = "1wIauG7PsNR9WZXgpEG6RswOUsQVqR2VR"
model_path="pipeline.pkl"

# 모델 다운로드 함수
@st.cache_data
def download_model():

    if not os.path.exists(model_path):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, model_path, quiet=False)
    return model_path

def run_sale() :

    # 모델 다운로드
    model_file = download_model()

    # 모델 로드
    model = joblib.load(model_file)

    st.markdown("<hr style='border: 1px solid #f0f5f9; margin: 15px 0;'>", unsafe_allow_html=True)

    st.subheader('🏠 아파트 실거래가 예측')

    st.markdown("<br>", unsafe_allow_html=True)

    st.text('아파트 정보를 입력하세요')
    region_select=sorted(['경기도성남시분당구', '경기도파주시', '경기도고양시덕양구', '경기도남양주시', '경기도평택시', '경기도가평군',
       '경기도용인시기흥구', '경기도수원시영통구', '경기도하남시', '경기도수원시권선구', '경기도안양시동안구',
       '경기도용인시수지구', '경기도안양시만안구', '경기도고양시일산서구', '경기도시흥시', '경기도양평군',
       '경기도화성시', '경기도오산시', '경기도광명시', '경기도의정부시', '경기도안산시단원구', '경기도김포시',
       '경기도안산시상록구', '경기도수원시팔달구', '경기도이천시', '경기도의왕시', '경기도부천시원미구',
       '경기도군포시', '경기도과천시', '경기도수원시장안구', '경기도용인시처인구', '경기도부천시소사구',
       '경기도성남시수정구', '경기도구리시', '경기도광주시', '경기도여주시', '경기도고양시일산동구', '경기도안성시',
       '경기도양주시', '경기도부천시오정구', '경기도포천시', '경기도동두천시', '경기도성남시중원구', '경기도연천군',
       '경기도 안양시동안구', '경기도 부천시원미구', '경기도 부천시소사구', '경기도 수원시팔달구',
       '경기도 성남시분당구', '경기도 부천시오정구', '경기도 성남시수정구', '경기도 의정부시', '경기도 수원시권선구',
       '경기도 성남시중원구', '경기도 수원시장안구', '경기도 고양시일산서구', '경기도 수원시영통구',
       '경기도 안양시만안구', '경기도 안산시단원구', '경기도 평택시', '경기도 고양시일산동구', '경기도 안산시상록구',
       '경기도 군포시', '경기도 하남시', '경기도 고양시덕양구', '경기도 가평군', '경기도 양평군',
       '경기도 남양주시', '경기도 용인시처인구', '경기도 오산시', '경기도 과천시', '경기도 동두천시',
       '경기도 광명시', '경기도 광주시', '경기도 구리시', '경기도 시흥시', '경기도 용인시기흥구',
       '경기도 파주시', '경기도 용인시수지구', '경기도 의왕시', '경기도 연천군', '경기도 포천시',
       '경기도 안성시', '경기도 화성시', '경기도 김포시', '경기도 이천시', '경기도 양주시', '경기도 여주시'])
    region=st.selectbox('지역',region_select)
    area=st.number_input('전용 면적 ( ㎡ )',min_value=0,value=100)
    floors=st.number_input('층',min_value=1,value=1)
    years=st.number_input('건축 년도',min_value=1900,value=2020)

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button('예측하기'):
        new_data = pd.DataFrame([[region, area, floors, years]], columns=['시군구명', '전용면적', '층', '건축년도'])
        y_pred = model.predict(new_data)

        pred_data = y_pred[0]

        if pred_data < 0:
            st.error('예측이 불가능한 데이터입니다.')
        else:
            pred_data = round(pred_data)
            if pred_data >= 10000:  # 1억 이상일 경우
                billions = pred_data // 10000
                millions = pred_data % 10000
                if millions == 0:
                    result = f'{billions}억원'
                else:
                    result = f'{billions}억 {millions:,}만원'
            else:  # 1억 미만일 경우
                result = f'{pred_data:,}만원'
            
            # 평수 계산
            pyeong = round(area / 3.305785, 2)
            
            st.success(f'예측된 실거래가는 {result} 입니다.')
            st.info(f'전용면적 {area}㎡는 약 {pyeong}평 입니다.')
            st.warning("주의사항: 본 앱의 예측 결과는 참고용이며, 실제 거래 시 반드시 전문가와 상담을 권장합니다.")


