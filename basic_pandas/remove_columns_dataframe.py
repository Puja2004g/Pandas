import numpy as np
import pandas as pd
from numpy.random import randn

my_data = randn(5, 2)
my_rows = ["apple", "banana", "sapodilla", "mango", "elderberry"]
my_cols = ["Longitude", "Latitude"]

my_df = pd.DataFrame(my_data, my_rows, my_cols)

my_df["Fresh/Stale"] = [True]*len(my_df)

my_df["available"] = [np.nan]*len(my_df)

my_df.insert(1, "Trees alive", [True]*len(my_df))

# remove a column permanently
# axis = 1 represents columns and axis = 0 represents rows
my_df.drop("available", axis=1, inplace=True)
# print(my_df)

my_df.drop("sapodilla", axis=0, inplace=True)
print(my_df)

