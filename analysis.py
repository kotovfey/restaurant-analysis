import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Смотрим первые строки
print(df.head())

# Создаём новую колонку — счет на человека
df["bill_per_person"] = df["total_bill"] / df["size"]

# Средний счет и чаевые
print("\nСредний счет:", df["total_bill"].mean())
print("Средние чаевые:", df["tip"].mean())

# Анализ по полу
print("\nСредние чаевые по полу:")
print(df.groupby("sex")["tip"].mean())

# Анализ по времени
print("\nСредний счет по времени:")
print(df.groupby("time")["total_bill"].mean())

# Анализ по размеру компании
print("\nСредний счет на человека по размеру компании:")
print(df.groupby("size")["bill_per_person"].mean())

# График
df.groupby("size")["bill_per_person"].mean().plot(kind="bar")

plt.title("Средний чек на человека vs размер компании")
plt.xlabel("Размер компании")
plt.ylabel("Счет на человека")

plt.show()