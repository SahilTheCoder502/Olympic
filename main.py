import streamlit as st
import pandas as pd
import numpy as np

import preprocessor,helper
df=pd.read_csv('athlete_events.csv.csv')
rg_df=pd.read_csv('noc_regions.csv')

df=preprocessor.preprocessor(df,rg_df)
st.sidebar.title('Olympics Analysis')

user_menu=st.sidebar.radio('Select an Option',('Medal Telly','Olympics Analysis','Country-wise Analysis'))

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