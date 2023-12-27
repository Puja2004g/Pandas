import pandas as pd

stuff = {
    'corporation': ['Apple', 'Google', 'Meta', 'Apple', 'Google', 'Meta'],
    'employee': ['John', 'April', 'Wes', 'Beth', 'Justin', 'Steph'],
    'salary': [200, 220, 190, 130, 120, 150]
}

my_df = pd.DataFrame(stuff)
print(my_df)

# grab a specific column
col = my_df['corporation']
print(col)

# counts elements
print(col.value_counts())

# get unique data
unique = col.unique()
print("unique data: ")
print(unique)

# unique data as dataframe
unique_df = pd.DataFrame(unique)
print("Unique dataframe: ")
print(unique_df)


# specific no. of unique data from a dataframe
head = unique_df.head(2)
print("First 2: ")
print(head)

tail = unique_df.tail(2)
print("Last 2: ")
print(tail)






