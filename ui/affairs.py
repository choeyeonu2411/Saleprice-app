import pandas as pd
import joblib 
import streamlit as st

region_to_dong = {
    '경기도 성남시분당구': ['야탑동', '구미동', '삼평동', '정자동', '서현동'],
    '경기도 시흥시': ['정왕동', '금곡동'],
    '경기도성남시분당구': ['야탑동', '구미동', '삼평동', '정자동', '서현동'],
    '경기도 부천시원미구': ['중동', '상동'],
    '경기도 파주시': ['와동동', '교하동'],
    '경기도안양시만안구': ['안양동'],
    '경기도남양주시': ['다산동'],
    '경기도고양시일산동구': ['장항동', '주엽동'],
    '경기도용인시기흥구': ['보정동'],
    '경기도 양평군': ['옥천면 신복리'],
    '경기도화성시': ['반송동'],
    '경기도안산시단원구': ['원곡동', '고잔동'],
    '경기도부천시원미구': ['중동', '상동'],
    '경기도군포시': ['산본동'],
    '경기도시흥시': ['정왕동', '금곡동'],
    '경기도 고양시일산동구': ['장항동', '주엽동'],
    '경기도 남양주시': ['다산동'],
    '경기도수원시장안구': ['영천동'],
    '경기도양평군': ['옥천면 신복리'],
    '경기도 안양시만안구': ['안양동'],
    '경기도안양시동안구': ['관양동', '호계동'],
    '경기도 화성시': ['반송동'],
    '경기도 고양시덕양구': ['향동동', '지축동'],
    '경기도수원시팔달구': ['인계동'],
    '경기도 안양시동안구': ['관양동', '호계동'],
    '경기도 수원시팔달구': ['인계동'],
    '경기도 안산시단원구': ['원곡동', '고잔동'],
    '경기도고양시일산서구': ['주엽동'],
    '경기도 용인시기흥구': ['보정동'],
    '경기도 수원시권선구': ['금곡동'],
    '경기도 고양시일산서구': ['주엽동'],
    '경기도 하남시': ['풍산동'],
    '경기도평택시': ['평택동'],
    '경기도 군포시': ['산본동'],
    '경기도 수원시장안구': ['영천동'],
    '경기도 오산시': ['오산동'],
    '경기도고양시덕양구': ['향동동', '지축동'],
    '경기도 평택시': ['평택동'],
    '경기도수원시권선구': ['금곡동'],
    '경기도파주시': ['와동동', '교하동'],
    '경기도오산시': ['오산동'],
    '경기도하남시': ['풍산동'],
    '경기도여주시': ['능곡동']
}

def run_affairs() :

    st.subheader('🏦 업무/상업용 실거래가 에측')
    st.text('상업오피스 정보를 입력하세요')

    
    # 지역 선택
    region_select = sorted(list(set(region_to_dong.keys())))
    region = st.selectbox('지역', region_select)

    # 선택된 지역에 해당하는 동 목록 가져오기
    available_dongs = sorted(list(set(region_to_dong.get(region, []))))

    # 동 선택
    region2 = st.selectbox('동', available_dongs)

    area=st.number_input('전용 면적 ( ㎡ )',min_value=0,value=30)

    trader_select=sorted(['법인', '개인', '기타', '공공기관'])
    trader=st.selectbox('매수자거래자정보',trader_select)
    
    if st.button('예측하기') :
        regressor=joblib.load('model/affairs.pkl')
        new_data = pd.DataFrame([[region,region2,area,trader ]], columns=['시군구명','읍면동리명','전용면적','매수자거래주체정보'])
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
            
            # 평수 계산
            pyeong = round(area / 3.305785, 2)
            
            st.success(f'예측된 실거래가는 {result} 입니다.')
            st.info(f'전용면적 {area}㎡는 약 {pyeong}평 입니다.')


