import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('f-c.csv',usecols=[1, 2])

print(df.head(3)) #pierwsze 3 wiersze

model = LinearRegression()
model.fit(df[['F']], df.C)
print(f'Wspolczynnik kierunkowy: {model.coef_}\nWyraz wolny: {model.intercept_}')

plt.scatter(df.F, df.C)
plt.plot(df.F, df.F*model.coef_ + model.intercept_, c='r')
plt.show()