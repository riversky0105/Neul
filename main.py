import streamlit as st
import pandas as pd
import plotly.express as px

# 앱 제목
st.title("📊 Google Drive 데이터 시각화 웹앱")

# 데이터 불러오기
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"데이터를 불러오는 데 실패했습니다: {e}")
        return None

df = load_data()

# 데이터가 로드되었을 경우
if df is not None:
    st.subheader("🔍 데이터 미리보기")
    st.dataframe(df)

    # 컬럼 선택
    st.subheader("🛠️ 시각화 설정")
    x_axis = st.selectbox("X축 열 선택", df.columns)
    y_axis = st.selectbox("Y축 열 선택", df.columns)

    # 그래프 종류 선택
    chart_type = st.selectbox("그래프 종류 선택", ["산점도 (scatter)", "선형 그래프 (line)", "막대 그래프 (bar)"])

    # 그래프 그리기
    st.subheader("📈 결과 시각화")
    if chart_type == "산점도 (scatter)":
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
    elif chart_type == "선형 그래프 (line)":
        fig = px.line(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
    elif chart_type == "막대 그래프 (bar)":
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
    
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("데이터를 불러오지 못했습니다. 링크를 확인해주세요.")

