from pandas import *
import matplotlib.pyplot as plt

data = read_csv("costRevenue.csv")

print(data.describe())

X = DataFrame(data, columns=["productionBudgetUSD"])
y = DataFrame(data, columns=["worldwideGrossUSD"])

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.5)
plt.title("Film Budget vs Global Revenue")
plt.xlabel("Worldwide Gross $")
plt.ylabel("Production Budget $")
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()
