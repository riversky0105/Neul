import pandas as pd
import plotly.express as px
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="데이터 시각화", layout="wide")

st.title("Plotly를 사용한 데이터 시각화 웹앱")

# Google Drive에서 데이터 불러오기
file_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data(file_url)

# 데이터 확인
st.subheader("데이터 미리보기")
st.dataframe(df)

# 컬럼 선택
numeric_columns = df.select_dtypes(include=["float", "int"]).columns.tolist()

x_col = st.selectbox("X축 선택", numeric_columns)
y_col = st.selectbox("Y축 선택", numeric_columns, index=1 if len(numeric_columns) > 1 else 0)
color_col = st.selectbox("컬러 기준 컬럼 선택 (선택 사항)", [None] + df.columns.tolist())

# Plotly 시각화
fig = px.scatter(
    df, x=x_col, y=y_col, color=color_col,
    title=f"{x_col} vs {y_col}",
    labels={x_col: x_col, y_col: y_col}
)

st.plotly_chart(fig, use_container_width=True)
