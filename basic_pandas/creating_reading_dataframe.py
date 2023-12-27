import numpy as np
import pandas as pd
from numpy.random import randn

# specifying rows = 4 and columns = 3
my_data = randn(4,3)
my_rows = ["A", "B", "C", "D"]
my_cols = ["Monday", "Tuesday", "Wednesday"]

# create dataframe
my_df = pd.DataFrame(my_data, my_rows, my_cols)
print(my_df)

# reading a CSV file
my_df2 = pd.read_csv("plots_and_charts/simple_dataframe.csv")
print(my_df2)

# read specific rows
print(my_df2.loc[0])
print(my_df2.loc[[0,5]])

# reading first 5 rows
print(my_df2.head())

# first 9 rows
print(my_df2.head(9))

# reading last 5 rows
print(my_df2.tail())

# last 9 rows
print(my_df2.tail(9))

# some basic info about the dataframe
print(my_df2.info())

# shape of rows and columns
print(my_df2.shape)

# no. of dimensions
print(my_df2.ndim)

# get the column datatypes
print(my_df2.dtypes)

# get statistics of the data
print(my_df2.describe())

# describe a specific column
print(my_df2['SAT'].describe())

# get specific column using brackets
print(my_df2['SAT'])

# get specific column using dot
print(my_df2.SAT)

# get specific column using location
print(my_df2.iloc[:, 0])