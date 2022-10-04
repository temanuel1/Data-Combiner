import pandas as pd

df = pd.read_csv("C:/Users/tyler/APL Projects/Data Combiner/fishy files/2020-2021(combined).csv")
# test_df = pd.read_csv("C:/Users/tyler/APL Projects/Data Combiner/fishy files/2019-01-01.csv")
print(df.head)
# print(df.size)
EuropeDataFrame = df[(cell_ll_lat < 63) & (cell_ll_lat > 30) & (cell_ll_lon < 35) & (cell_ll_lon > -18)]
print(EuropeDataFrame.size)