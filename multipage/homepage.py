import streamlit as st
import plotly.express as px 

st.set_page_config(
    layout="wide",
    page_title='Tips HomePage',
    page_icon='🪙'
)

df = px.data.tips()
num = df.describe()
cat = df.describe(include = 'O')


#Side bar
st.sidebar.success('select page above')
st.markdown('<h1 style="text-align: center; color : black;">Home Page For Dash Board</h1>', unsafe_allow_html= True)

tab1, tab2= st.tabs(["🗓️ Data",'📈 Describtive Stats'])


with tab1:
    col1, col2, col3= st.columns([3,4,3])
    with col2:
        st.markdown('<h3 style="text-align: center; color : black;">Dataset</h3>', unsafe_allow_html=True)
        st.dataframe(df.copy(), 800, 500)


with tab2:
    col1, col2, col3= st.columns([6,0.5,6])
    with col1:
        st.subheader('Numerical Describtive Statistics')
        st.dataframe(num.T,700, 150)

    with col3:
        st.subheader('Categorical Describtive Statistics')
        st.dataframe(cat.T, 500, 200)
