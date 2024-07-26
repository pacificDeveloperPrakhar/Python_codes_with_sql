import pandas as pd
datafetched=pd.read_csv("data.csv",delimiter=';',usecols=['Username'])
print(datafetched)