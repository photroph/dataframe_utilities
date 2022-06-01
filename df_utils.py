import pandas as pd


def dropDuplicatedRankCols(df: pd.DataFrame):
    df_rank = df.rank()
    tmp = df_rank.T.drop_duplicates().T
    return df[tmp.columns]
