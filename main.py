import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="Plotly 시각화 앱", layout="wide")
st.title("📊 Plotly 시각화 웹앱")

# 데이터 불러오기 함수
@st.cache_data  # Streamlit <1.18 버전이면 @st.cache 로 변경
def load_data():
    try:
        url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"데이터를 불러오는 중 오류가 발생했습니다: {e}")
        return pd.DataFrame()

# 데이터 불러오기
df = load_data()

# 유효성 확인
if df.empty:
    st.warning("데이터가 비어있습니다. 링크나 파일 형식을 확인하세요.")
    st.stop()

# 데이터 미리보기
st.subheader("🔍 데이터 미리보기")
st.dataframe(df.head(), use_container_width=True)

# 수치형 컬럼 추출
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

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
    st.write("🔍 수치형 컬럼 확인:", numeric_cols)

