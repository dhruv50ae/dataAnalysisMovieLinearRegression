from pandas import *
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = read_csv("cost-revenue-movies.csv")

x = DataFrame(data, columns=["productionBudgetUSD"])
y = DataFrame(data, columns=["worldwideGrossUSD"])

# plt.figure(figsize=(10, 6))
# plt.scatter(x, y, alpha=0.3)
# plt.title("Film Cost vs Global Revenue")
# plt.xlabel("Production Budget ($)")
# plt.ylabel("Worldwide Gross ($)")
# plt.ylim(0, 3000000000)
# plt.xlim(0, 450000000)
# plt.show()

regression = LinearRegression()
regression.fit(x, y)
gradient = regression.coef_
print(gradient)
intercept = regression.intercept_
print(intercept)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.3)
plt.plot(x, regression.predict(x), color="red", linewidth=4)
plt.title("Film Cost vs Global Revenue")
plt.xlabel("Production Budget ($)")
plt.ylabel("Worldwide Gross ($)")
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()

print(regression.score(x, y))