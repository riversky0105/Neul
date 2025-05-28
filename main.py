my-streamlit-app/
├── app.py
└── requirements.txt

import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="Plotly 시각화 앱", layout="wide")
st.title("📊 Plotly 시각화 웹앱")

# 데이터 불러오기 함수
@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
    df = pd.read_csv(url)
    return df

# 데이터 불러오기
df = load_data()

# 데이터 미리보기
st.subheader("🔍 데이터 미리보기")
st.dataframe(df.head(), use_container_width=True)

# 수치형 컬럼만 추출
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

# 시각화 옵션
if len(numeric_cols) >= 2:
    st.subheader("⚙️ 시각화 옵션 선택")
    col1, col2 = st.columns(2)

    with col1:
        x_col = st.selectbox("X축 컬럼 선택", numeric_cols)

    with col2:
        y_col = st.selectbox("Y축 컬럼 선택", numeric_cols)

    # 시각화 생성
    fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("시각화를 위해 수치형 컬럼이 2개 이상 필요합니다.")
