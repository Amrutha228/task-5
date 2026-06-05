import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print(df.head())
print(df.shape)

product_sales = df.groupby("Product")["Sales"].sum()

product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

region_sales = df.groupby("Region")["Sales"].sum()

region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Region")
plt.ylabel("")
plt.show()