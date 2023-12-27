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

# add a column to index
my_df.set_index("Breeds", inplace=True)
print(my_df)


# reset index
my_df.reset_index(inplace=True)
print(my_df)


# delete old header column
my_df.drop("Fresh/Stale", axis=1, inplace=True)
print(my_df)