import pandas as pd

def extract():
    return pd.read_csv('data.csv')

def transform(df):
    return df.dropna()

def load(df):
    df.to_sql('table', con='postgresql://user:password@host/db')

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)
