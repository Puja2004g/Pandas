import numpy as np
import pandas as pd
from numpy.random import randn

my_data = randn(5, 2)
my_rows = ["apple", "banana", "sapodilla", "mango", "elderberry"]
my_cols = ["Longitude", "Latitude"]

my_df = pd.DataFrame(my_data, my_rows, my_cols)

# add a new column in a dataframe
count = [10, 23, 25, 12, 89]
my_df["Total count"] = count

# adding a default value to dataframe
my_df["Fresh/Stale"] = [True]*len(my_df)

# adding null values
my_df["available"] = [np.nan]*len(my_df)

# adding a column using insert function
my_df.insert(1, "Trees alive", [True]*len(my_df))
# print(my_df)

# add a column using assign function
my_df2 = my_df.assign(Buy = [False]*len(my_df))
print(my_df2)
