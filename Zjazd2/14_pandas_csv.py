import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df0 = pd.read_csv('weight-height.csv', delimiter=';')

df = df0.copy()

print(df)
print(type(df))

df.Height *= 2.54
df.Weight /= 2.2
print(df.head(3))   # pierwsze 3 wiersze

print('\nWykres')
plt.hist(df.Weight, 50)
plt.show()

# print(df.describe())



