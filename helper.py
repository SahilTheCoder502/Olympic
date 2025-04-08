import pandas as pd
import numpy as np
import plotly.express as px
def medal_tally(df):
    medal_tally=df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby('region').sum()[['Bronze', 'Gold', 'Silver']].sort_values('Gold',
                                                                                                ascending=False).reset_index()
    medal_tally['total']=medal_tally['Gold']+medal_tally['Silver']+medal_tally['Bronze']
    medal_tally['Gold']=medal_tally['Gold'].astype('int')
    medal_tally['Silver'] = medal_tally['Silver'].astype('int')
    medal_tally['bronze'] = medal_tally['Bronze'].astype('int')
    return medal_tally
def country_year_list(df):
    year = df['Year'].unique().tolist()
    year.sort()
    year.insert(0,'overall')
    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'overall')
    return year,country


def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'overall' and country == 'overall':
        temp_df = medal_df
    if year == 'overall' and country != 'overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != 'overall' and country == 'overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'overall' and country != 'overall':
        temp_df = medal_df[(medal_df['region'] == country) & (medal_df['Year'] == int(year))]

    if flag == 1:
        x_df = temp_df.groupby('Year').sum()[['Bronze', 'Gold', 'Silver']].sort_values('Year').reset_index()
    else:
        x_df = temp_df.groupby('region').sum()[['Bronze', 'Gold', 'Silver']].sort_values('Gold',
                                                                                         ascending=False).reset_index()

    x_df['total'] = x_df['Gold'] + x_df['Silver'] + x_df['Bronze']
    x_df['Gold'] =  x_df['Gold'].astype('int')
    x_df['Silver'] =  x_df['Silver'].astype('int')
    x_df['Bronze'] = x_df['Bronze'].astype('int')
    return x_df

def partitioning_nations_over_years(df):
    nations_over_counttime = df.drop_duplicates(['Year', 'region'])['Year'].value_counts().reset_index().sort_values(
        'Year')
    nations_over_counttime.rename(columns={'Year':'Editions','count':'Number of Countries'}, inplace=True)
    return nations_over_counttime

