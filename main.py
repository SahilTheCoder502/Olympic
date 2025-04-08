import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

import preprocessor,helper
df=pd.read_csv('athlete_events.csv.csv')
rg_df=pd.read_csv('noc_regions.csv')

df=preprocessor.preprocessor(df,rg_df)
st.sidebar.title('Olympics Analysis')

user_menu=st.sidebar.radio('Select an Option',('Medal Telly','Overall Analysis','Country-wise Analysis'))

# st.dataframe(df,use_container_width=True)
if user_menu=='Medal Telly':
    st.sidebar.header('Medal Telly')
    year,country=helper.country_year_list(df)
    selected_year=st.sidebar.selectbox('Select year',year)
    selected_country=st.sidebar.selectbox('Select country', country)
    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_country == 'overall' and selected_year=='overall':
        st.title('Overall  Tally')
    if selected_country == 'overall' and selected_year!='overall':
        st.title('Medal  Tally in' + ' ' + str(selected_year))
    if selected_country != 'overall' and selected_year=='overall':
        st.title('Medal Tally in' + ' ' + selected_year)
    if selected_country != 'overall' and selected_year!='overall':
        st.title('Medal Tally in' + ' '+  str(selected_year) + ' '+   'in' +' ' + selected_country)
    st.table(medal_tally)
if user_menu=='Overall Analysis':
    editions=df['Year'].unique().shape[0] - 1
    cities=df['City'].unique().shape[0]
    sports=df['Sport'].unique().shape[0]
    events=df['Event'].unique().shape[0]
    athlete=df['Name'].unique().shape[0]
    nations=df['region'].unique().shape[0]
    st.title('Top Statistics')
    col1,col2,col3=st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sport')
        st.title(sports)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Athlete')
        st.title(athlete)
    with col3:
        st.header('Nations')
        st.title(nations)

    nations_over_counttime=helper.partitioning_nations_over_years(df)

    fig = px.line(nations_over_counttime, x='Editions', y='Number of Countries')
    st.title('Partitioning of Nations Over the Years')
    st.plotly_chart(fig)



