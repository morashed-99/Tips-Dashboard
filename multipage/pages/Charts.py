import streamlit as st
import plotly.express as px

st.set_page_config(
        layout = 'wide',
        page_title = 'DashBoard',
        page_icon= '📊'
)

tab1, tab2 = st.tabs(['📈  Numerical Charts','📊 Categorical Charts'])
df = px.data.tips()


with tab1:
    st.markdown('<h3 style="text-align: center; color : black;">Distribution of Numerical features</h3>', unsafe_allow_html=True)
    col= st.selectbox('select feature to see its distribution', ['total_bill', 'tip'], key=10)
    with st.container():
        col1, col2, col3 = st.columns([5,1,5])
        fig= px.histogram(df, x= col, color_discrete_sequence=px.colors.qualitative.Antique)
        col1.plotly_chart(fig, use_container_width= True)

        fig= px.box(df, x= col,color_discrete_sequence=px.colors.qualitative.Antique )
        col3.plotly_chart(fig, use_container_width= True)
        
        st.write('<h3 style="text-align: center; color : black;">Correlation Between Numerical features with filters</h3>', unsafe_allow_html=True)

    with st.container():
        col4, col5, col6 = st.columns([6,1,6])
        # col4
        # Adding a placeholder option
        options = ['None'] + df['time'].unique().tolist()
        time= col4.selectbox('select Meal Time', options, key=7)
        new_df2= df[df['time']==time]
        fig= px.scatter(new_df2, x='total_bill', y= 'tip', size= 'size',size_max=20,
                       color= 'sex', title= f'correlation between total bill and tips on {time}',color_discrete_sequence=px.colors.qualitative.Antique)
        col4.plotly_chart(fig, use_container_width=True)

        # col6
        size= col6.radio('select how many dishes', df['size'].unique(), key=3, horizontal=True)
        new_df1= df[df['size']==size]
        fig= px.line(new_df1.sort_values(by='total_bill'), x= 'total_bill', y='tip',color='sex',
                    title= f'correlation between total bill and tips on {time}',color_discrete_sequence=px.colors.qualitative.Antique)
        col6.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown('<h3 style="text-align: center; color : black;">Distribution of Categorical features</h3>', unsafe_allow_html=True)
    col= st.selectbox('select feature to see the distribution',['sex', 'day', 'time', 'size'] ,key=11)
    # dist part
    with st.container():
        col1, col2, col3=st.columns([5,1,5])
        fig= px.histogram(df, x= col, color_discrete_sequence=px.colors.qualitative.Antique)
        col1.plotly_chart(fig, use_container_width=True)

        fig= px.pie(df, names= col, color_discrete_sequence=px.colors.qualitative.Antique, hole=.3).update_traces(textinfo='value')
        col3.plotly_chart(fig,use_container_width=True)
        st.write('<h3 style="text-align: center; color : black;">Some BiVariate Analysis</h3>', unsafe_allow_html=True)

    with st.container():
        col1,col2,col3= st.columns([5,1,5])
        #col1
        day= col1.selectbox('Select Day', df['day'].unique(), key= 4 )
        new_df1= df[df['day']== day]
        fig = px.histogram(new_df1, x='total_bill',color = 'sex',
                           title=f'totalt bill for {day}day'.title(), color_discrete_sequence=px.colors.qualitative.Antique)
        col1.plotly_chart(fig, use_container_width=True)


        size= col1.radio('Select How many Dishes', sorted(df['size'].unique()),3,  key=6, horizontal=True)
        new_df1 = df[df['size'] == size]
        fig= px.pie(new_df1, names='time',title=f'count of each meal time according to {size} dishes'.title(),
                     color_discrete_sequence=px.colors.qualitative.Antique, hole=0.32).update_traces(textinfo='value')
        col1.plotly_chart(fig,  use_container_width=True)


        # col3 
        # time= col3.selectbox('select Meal Time', df['time'].unique(), key=5)
        # new_df2 = df[df['time'] == time]

        # fig = px.scatter(new_df2, x='total_bill', y = 'tip', size = 'size', size_max=20,color = 'sex',
        #                  title=f'correlation between total bill and tips on {time}', color_discrete_sequence=px.colors.qualitative.Antique)
        # col3.plotly_chart(fig,use_container_width=True)
        gender= col3.radio('Select  Gender', df['sex'].unique(), key=8, horizontal=True)
        new_df2 = df[df['sex'] == gender]
        fig= px.sunburst(new_df2, path=['day', 'time', 'size'], color = 'tip',
                          title=f'counting over day, time and size over tips for only {gender}'.title(),color_continuous_scale= px.colors.sequential.Brwnyl)
        col3.plotly_chart(fig,use_container_width=True)
        fig = px.treemap(df,path=['day', 'time', 'size'], color = 'tip', color_continuous_scale= px.colors.sequential.Brwnyl, height=550 ,
                         title=f'counting over day, time and size over tips for only {gender}'.title())
        col3.plotly_chart(fig,use_container_width=True)
