from pandas import *
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = read_csv("costRevenue.csv")

print(data.describe())

X = DataFrame(data, columns=["productionBudgetUSD"])
y = DataFrame(data, columns=["worldwideGrossUSD"])

regression = LinearRegression()
regres = regression.fit(X, y)
print(regres)
# Slope Coefficient
coefficient = regression.coef_
print(coefficient)
# Line intercept
intercept = regression.intercept_
print(intercept)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.5)
plt.plot(X, regression.predict(X), color="red")
plt.title("Film Budget vs Global Revenue")
plt.xlabel("Worldwide Gross $")
plt.ylabel("Production Budget $")
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()

goodnessOfFit = regression.score(X, y)

print(goodnessOfFit)
