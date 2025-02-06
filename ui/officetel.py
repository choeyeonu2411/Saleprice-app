import pandas as pd
import joblib 
import streamlit as st

def run_office() :

    st.subheader('오피스텔 실거래가 에측')
    st.text('아파트 정보를 입력하세요')
    region_select=sorted(['경기도 수원시권선구', '경기도 화성시', '경기도 시흥시', '경기도 오산시', '경기도 고양시일산동구',
       '경기도 하남시', '경기도용인시처인구', '경기도의정부시', '경기도수원시영통구', '경기도안양시동안구',
       '경기도 남양주시', '경기도김포시', '경기도 수원시팔달구', '경기도 평택시', '경기도안산시상록구',
       '경기도고양시일산동구', '경기도 과천시', '경기도 김포시', '경기도 용인시처인구', '경기도 고양시덕양구',
       '경기도 파주시', '경기도 부천시원미구', '경기도 의정부시', '경기도 안양시동안구', '경기도 성남시수정구',
       '경기도 안양시만안구', '경기도 성남시중원구', '경기도 성남시분당구', '경기도용인시기흥구', '경기도시흥시',
       '경기도화성시', '경기도부천시원미구', '경기도남양주시', '경기도평택시', '경기도 용인시기흥구',
       '경기도 수원시영통구', '경기도 군포시', '경기도하남시', '경기도 안산시단원구', '경기도성남시분당구',
       '경기도 용인시수지구', '경기도성남시수정구', '경기도수원시팔달구', '경기도안산시단원구', '경기도 이천시',
       '경기도고양시덕양구', '경기도수원시권선구', '경기도군포시', '경기도오산시', '경기도안양시만안구',
       '경기도 안성시', '경기도 구리시', '경기도 여주시', '경기도구리시', '경기도광명시', '경기도용인시수지구',
       '경기도 부천시소사구', '경기도부천시소사구', '경기도성남시중원구', '경기도의왕시', '경기도이천시',
       '경기도 수원시장안구', '경기도파주시', '경기도 의왕시', '경기도 광명시', '경기도 안산시상록구',
       '경기도 고양시일산서구', '경기도고양시일산서구', '경기도여주시', '경기도안성시', '경기도과천시',
       '경기도광주시', '경기도 포천시', '경기도 가평군', '경기도수원시장안구', '경기도 양평군', '경기도 광주시',
       '경기도 부천시오정구', '경기도 연천군', '경기도 동두천시', '경기도 양주시', '경기도양주시', '경기도포천시',
       '경기도부천시오정구'])
    region=st.selectbox('지역',region_select)
    area=st.number_input('전용 면적',min_value=0,value=10)
    floors=st.number_input('층',min_value=1,value=1)
    years=st.number_input('건축 년도',min_value=1900,value=2000)
    
    if st.button('예측하기') :
        regressor=joblib.load('model/officetel.pkl')
        new_data = pd.DataFrame([[region, area, floors,years]], columns=['시군구명','전용면적','층','건축년도'])
        y_pred=regressor.predict(new_data)

        pred_data=y_pred[0]

        if pred_data<0 :
            st.error('예측이 불가능한 데이터 입니다.')
        else :
            pred_data = round(pred_data)
            if pred_data >= 10000 :  # 1억 이상일 경우
                billions = pred_data // 10000
                millions = pred_data % 10000
                if millions == 0:
                    result = f'{billions}억원'
                else:
                    result = f'{billions}억 {millions:,}만원'
            else:  # 1억 미만일 경우
                result = f'{pred_data:,}만원'
            
            st.success(f'예측된 실거래가는 {result} 입니다.')


