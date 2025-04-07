import pandas as pd
import numpy as np

def preprocessor(df,rg_df):

    df = df[df['Season'] == 'Summer']
    df = df.merge(rg_df, on='NOC', how='left')
    df.drop_duplicates( inplace=True)
    df=pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
    return df





