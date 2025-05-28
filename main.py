import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.set_page_config(page_title="Plotly 시각화 앱", layout="wide")
st.title("📊 Plotly 시각화 웹앱")

# 데이터 불러오기 함수
@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
    df = pd.read_csv(url)
    return df

# 데이터 로딩
df = load_data()

# 데이터 확인
st.subheader("🔍 데이터 미리보기")
st.dataframe(df.head(), use_container_width=True)

# 수치형 컬럼 필터링
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

if len(numeric_cols) >= 2:
    st.subheader("⚙️ 시각화 옵션 선택")
    col1, col2 = st.columns(2)

    with col1:
        x_col = st.selectbox("X축 컬럼 선택", numeric_cols, index=0)

    with col2:
        y_col = st.selectbox("Y축 컬럼 선택", numeric_cols, index=1)

    # Plotly 산점도 그리기
    fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}", size_max=60)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("데이터에 시각화할 수치형 컬럼이 2개 이상 있어야 합니다.")
