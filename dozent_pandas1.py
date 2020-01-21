import pandas as pd

df = pd.read_csv('data/astronauts.csv', delimiter = ',')

# print(df)
# print(df.head(3))
# print(df.tail(3))
# print(df.describe())

# print(df.columns)

# print(df['Year'])
# print(df[['Name', 'Year', 'Gender']])
# print(len(df))

# print(df.iloc[0])
#
# ser = df.iloc[0]
# print(ser['Name'])

# print(df.iloc[-1])

# for row in df.iterrows():
    # # index
    # print(row[0])
    # # daten (Series)
    # print(row[1]['Name'])

# year = df['Year'] > 1990

# print(year)

# print(df[year])

print(df[df['Year'] > 1990]['Name'])
