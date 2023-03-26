import pandas as pd

# create the data frame
df = pd.DataFrame({
    '1st Term Students': [210, 25, 102, 74, 41, 18, 0, 10],
    '2nd Term Students': [133, 39, 73, 63, 18, 13, 5, 0],
    '3rd Term Students': [64, 11, 24, 31, 12, 8, 0, 0],
}, index=['PCOM', 'BCOM', 'PM', 'BA', 'GLM', 'FS', 'DXD', 'BK'])

# convert the data frame to a list of rows
rows = df.values.tolist()

# print the list of rows
print(rows)