import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('otodom.csv')
print(df)
print(df.describe().T.to_string())

# sns.heatmap(df.iloc[:, 2:].corr(), annot=True)
# plt.show()
#
# plt.hist(df.price, bins=10)
# # plt.show()
#
# sns.histplot(df.price, bins=50)
# plt.show()

plt.scatter(df.price, df.space)
plt.show()

q1 = df.describe().T.loc['price', '25%']
q3 = df.describe().T.loc['price', '75%']
print(f'cena na koncu q1 to: {q1}')
print(f'cena na koncu q3 to: {q3}')

df1 = df[(df.price >= q1) & (df.price <= q3)]
sns.histplot(df1.price)
plt.show()

plt.scatter(df1.price, df1.space)
plt.show()

X = df1.iloc[:, 2:]
y = df1.price

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(model.coef_, X.columns))

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
y_pred = model.predict(X_test)
print(mean_squared_error(y_test, y_pred))
print(mean_absolute_error(y_test,y_pred))
