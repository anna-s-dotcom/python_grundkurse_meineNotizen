# Finde heraus, wie viele (und welche) Frauen mehr als einen Weltraumgänge (Space Walks) hatten.

import pandas as pd

df = pd.read_csv('data/astronauts.csv')

#fem_bool = df['Gender'] == 'Female'
#sw_bool = df['Space Walks'] > 0
#fem_sw = fem_bool & sw_bool

df2 = df[fem_sw]
print(df2[['Name', 'Space Walks']])

#df3 = df[(df['Gender'] == 'Female') & (df['Space Walks'] > 1)]
#print(df3[['Name', 'Space Walks']])

# print(df[fem_bool])

df2.to_html('data/spacewalks.html')
df2.to_csv('data/spacewalks.csv')
df2.to_json('data/spacewalks.json')


print(df.sort_values('Space Walks', ascending = True)[['Name', 'Space Walks']])
