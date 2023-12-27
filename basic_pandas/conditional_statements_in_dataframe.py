import numpy as np
import pandas as pd
from numpy.random import randn

my_data = randn(5, 2)
my_rows = ["apple", "banana", "sapodilla", "mango", "elderberry"]
my_cols = ["Longitude", "Latitude"]

my_df = pd.DataFrame(my_data, my_rows, my_cols)
count = [10, 23, 25, 10, 89]
Fruits = ["Golden delicious", "Red banana", "Brown Sugar", "Alphonso", "Black beauty"]
my_df["Total count"] = count
my_df["Breeds"] = Fruits
my_df["Fresh/Stale"] = [True]*len(my_df)

# print(my_df)

# return booleans
print(my_df == 10)

# returns actual data
print(my_df[my_df == 10])

# run into a specific column
print(my_df[my_df == 10]["Total count"])

# run into multiple column
print(my_df[my_df == 10][["Total count", "available"]])


# multiple conditional statements

# and / &
print(my_df[(my_df["Breeds"]=="Alphonso") & (my_df["Total count"]==10)])

# get length
print(len(my_df[(my_df["Breeds"]=="Alphonso") & (my_df["Total count"]==10)]))

# or/ |
print(my_df[(my_df["Breeds"]=="Alphonso") | (my_df["Total count"]==10)])

# get length
print(len(my_df[(my_df["Breeds"]=="Alphonso") | (my_df["Total count"]==10)]))

# return a specific column
print(my_df[(my_df["Breeds"]=="Alphonso") | (my_df["Total count"]==10)]["Longitude"])



