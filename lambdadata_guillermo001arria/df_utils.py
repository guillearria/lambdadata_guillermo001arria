import pandas as pd

def check_nulls(df):
    return df.isnull().sum()

def list_to_column(df,name,li):
    X = df.copy()
    se = pd.Series(li)
    X[name] = se.values
    return X
