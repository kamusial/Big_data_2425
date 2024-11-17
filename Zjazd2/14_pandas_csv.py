import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

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

plt.hist(df.query('Gender=="Male"').Weight, 50)
# plt.show()
plt.hist(df.query('Gender=="Female"').Weight, 50)
plt.show()
print('\nWykresy Seaborn')
sns.histplot(df.query('Gender=="Male"').Weight)
sns.histplot(df.query('Gender=="Female"').Weight)
plt.show()

# zamiana gender na dane numeryczne
df = pd.get_dummies(df)
print(df.head(3))
del df['Gender_Male']
print(df.head(3))
df = df.rename(columns={'Gender_Female': 'Gender'})
# print(df.describe())
print(df.head(3))
# False - facet, True - kobieta

# algorytm
model = LinearRegression()
model.fit(df[['Height', 'Gender']]   , df['Weight']       )
print(model.coef_)    # wspolczynnkik kierunkowy
print(model.intercept_)    # wyraz wolny

print(f'Weight = Height * {model.coef_[0]} + Gender * {model.coef_[1]} + {model.intercept_}')



