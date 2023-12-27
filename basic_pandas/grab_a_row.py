import numpy as np
import pandas as pd
from numpy.random import randn

my_data = randn(5, 2)
my_rows = ["apple", "banana", "sapodilla", "mango", "elderberry"]
# my_rows = [0,1,2,3,4]
my_cols = ["Longitude", "Latitude"]

my_df = pd.DataFrame(my_data, my_rows, my_cols)

my_df["Fresh/Stale"] = [True]*len(my_df)

my_df["available"] = [np.nan]*len(my_df)
# print(my_df)

# get a specific row
# print(my_df.loc["apple"])

# it works only in case of numeric row names
# print(my_df.iloc[1])


# grab a specific point
# row=apple and column=latitude
print(my_df.loc["apple", "Latitude"])

# grab a specific subset
print(my_df.loc[["apple", "mango"], ["Longitude", "Fresh/Stale"]])