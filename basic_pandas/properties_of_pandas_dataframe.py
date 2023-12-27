import pandas as pd

df = pd.read_csv("plots_and_charts/simple_dataframe.csv")

# counting the distinct values : descending
print(df['GPA'].value_counts())

# counting distinct values : ascending
print(df['GPA'].value_counts(ascending=True))

# select names with NaN
print(df['GPA'].value_counts(dropna=False))

# get percentage
print(df['GPA'].value_counts(normalize=True))

# count specific items
print(df['GPA'].value_counts()[3.28])

# group by size
print(df.groupby("SAT").size())

# group by count
print(df.groupby("SAT").count())

# count of all columns across all columns
print(df.apply(pd.value_counts))

