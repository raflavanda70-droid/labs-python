import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")

# Загрузка данных
sales_df = pd.read_excel("S7_sales.xlsx", engine="openpyxl")
airports_df = pd.read_csv("airports.dat.csv", header=None)

airports_df.columns = ["ID", "Name", "City", "Country", "IATA", "ICAO",
                       "Latitude", "Longitude", "Altitude", "Timezone",
                       "DST", "TZ", "Type", "Source"]

merged_df = sales_df.merge(airports_df, left_on="ORIG_CITY_CODE", right_on="IATA", how="left")

print("Описательные статистики:")
print(sales_df.describe())
print("\nПропущенные значения:")
print(sales_df.isnull().sum())

#Сезонность
sales_df["ISSUE_DATE"] = pd.to_datetime(sales_df["ISSUE_DATE"])
sales_df["MONTH"] = sales_df["ISSUE_DATE"].dt.month
monthly_stats = sales_df.groupby("MONTH").agg({
    "REVENUE_AMOUNT": "sum",
    "FLIGHT_DATE_LOC": "count"
}).reset_index()

#Прогноз
daily_sales = sales_df.groupby("ISSUE_DATE").agg({"REVENUE_AMOUNT": "sum"}).reset_index()
daily_sales["DAYS"] = (daily_sales["ISSUE_DATE"] - daily_sales["ISSUE_DATE"].min()).dt.days
X = daily_sales[["DAYS"]]
y = daily_sales["REVENUE_AMOUNT"]
model = LinearRegression()
model.fit(X, y)
future_day = X["DAYS"].max() + 30
future_pred = model.predict([[future_day]])
print(f"\n Прогноз суммы продаж через 30 дней: {int(future_pred[0])} руб.")

top_airports = merged_df.groupby("Name").agg({
    "REVENUE_AMOUNT": "sum",
    "FLIGHT_DATE_LOC": "count"
}).sort_values("REVENUE_AMOUNT", ascending=False).head(10)

fop_means = sales_df.groupby("FOP_TYPE_CODE")["REVENUE_AMOUNT"].mean().sort_values()
pax_counts = sales_df["PAX_TYPE"].value_counts()
pax_means = sales_df.groupby("PAX_TYPE")["REVENUE_AMOUNT"].mean()

#Графики
plt.figure(figsize=(12, 6))
sales_df["REVENUE_AMOUNT"].plot.hist(bins=30, color='blue', edgecolor='black')
plt.title("Распределение суммы продаж", fontsize=16)
plt.xlabel("Сумма")
plt.ylabel("Количество записей")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x=top_airports["REVENUE_AMOUNT"], y=top_airports.index,color="violet" )
plt.title("Топ-10 аэропортов по выручке", fontsize=16)
plt.xlabel("Сумма продаж ")
plt.ylabel("Аэропорт")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_stats, x="MONTH", y="REVENUE_AMOUNT", marker="o", color="teal")
plt.title("Сезонность по сумме продаж", fontsize=16)
plt.xlabel("Месяц (1–12)")
plt.ylabel("Сумма (в рублях)")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_stats, x="MONTH", y="FLIGHT_DATE_LOC", marker="s", color="orange")
plt.title("Сезонность по количеству перелетов", fontsize=16)
plt.xlabel("Месяц (1–12)")
plt.ylabel("Число перелетов")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x=pax_means.index, y=pax_means.values, palette="coolwarm")
plt.title("Средняя сумма по типу пассажира", fontsize=16)
plt.xlabel("Тип пассажира")
plt.ylabel("Сумма (в рублях)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
sns.barplot(x=fop_means.values, y=fop_means.index, color="steelblue")
plt.title("Средняя сумма по способу оплаты", fontsize=16)
plt.xlabel("Сумма (в рублях)")
plt.ylabel("Способ оплаты")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(X, y, label="Фактические данные", alpha=0.6, color="gray")
plt.plot(X, model.predict(X), color="red", label="Линейный тренд")
plt.title("Прогноз суммы продаж", fontsize=16)
plt.xlabel("Дней с начала периода")
plt.ylabel("Сумма (в рублях)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(pax_counts.values, labels=pax_counts.index, autopct="%1.1f%%", textprops={'fontsize': 12})
plt.title("Распределение по типу пассажиров", fontsize=16)
plt.tight_layout()
plt.show()