import pandas as pd

stuff = {
    'corporation': ['Apple', 'Google', 'Meta', 'Apple', 'Google', 'Meta'],
    'employee': ['John', 'April', 'Wes', 'Beth', 'Justin', 'Steph'],
    'salary': [200, 220, 190, 130, 120, 150]
}

my_df = pd.DataFrame(stuff)
print(my_df)

# sort in ascending order
print("Ascending order salary ")
print(my_df.sort_values('salary'))

# sort in descending order
print("Descending order salary ")
print(my_df.sort_values('salary', ascending=False))

# sort in alphabetical order ascending
print("Ascending order corporation")
print(my_df.sort_values('corporation'))

# sort in alphabetical descending
print("Descending order corporation ")
print(my_df.sort_values('corporation', ascending=False))



