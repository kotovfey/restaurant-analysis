import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

print("Первые строки:")
print(df.head())
print("\nСредний счет:")
print(df["total_bill"].mean())

print("\nСредние чаевые:")
print(df["tip"].mean())

print("\nСредние чаевые по полу:")
print(df.groupby("sex")["tip"].mean())

print("\nСредний счет по времени дня:")
print(df.groupby("time")["total_bill"].mean())

print("\nСредний счет в зависимости от размера компании:")
print(df.groupby("size")["total_bill"].mean())
print("\nКолонки:")
print(df.columns)

print("\nИнформация о данных:")
print(df.info())
print(df.head)
df["bill_per_person"] = df["total_bill"] / df["size"]

print("\nСредний счет на человека:")
print(df["bill_per_person"].mean())

print("\nСчет на человека по размеру компании:")
print(df.groupby("size")["bill_per_person"].mean())
import matplotlib.pyplot as plt

df.groupby("size")["bill_per_person"].mean().plot(kind="bar")

plt.title("Средний чек на человека vs размер компании")
plt.xlabel("Размер компании")
plt.ylabel("Счет на человека")

plt.show()