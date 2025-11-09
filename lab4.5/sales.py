import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_excel('sales_data.xlsx', header=1)

df.columns = df.columns.str.strip().str.lower()

# Преобразование даты
df['дата'] = pd.to_datetime(df['дата'])
df['год-мес'] = pd.to_datetime(df['год-мес'], format='%Y%m')

df['средняя_цена'] = df['продажи'] / df['количество']
df['маржа'] = df['продажи'] - df['себестоимость']

grouped = df.groupby(['товар', 'точка', 'год-мес']).agg({
    'количество': 'sum',
    'продажи': 'sum',
    'себестоимость': 'sum'
}).reset_index()

grouped['средняя_цена'] = grouped['продажи'] / grouped['количество']
grouped['маржа'] = grouped['продажи'] - grouped['себестоимость']

plt.figure(figsize=(12, 6))
for product in grouped['товар'].unique():
    temp = grouped[grouped['товар'] == product]
    plt.plot(temp['год-мес'], temp['продажи'], label=product)
plt.title('Динамика продаж по товарам')
plt.xlabel('Период')
plt.ylabel('Продажи')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

avg_sales_point = df.groupby('точка')['продажи'].mean().sort_values()
sns.barplot(x=avg_sales_point.values, y=avg_sales_point.index)
plt.title('Средние продажи на точку')
plt.xlabel('Средние продажи')
plt.ylabel('Точка')
plt.tight_layout()
plt.show()

total_turnover = df.groupby('год-мес')['продажи'].sum().reset_index()
plt.figure(figsize=(10, 5))
plt.plot(total_turnover['год-мес'], total_turnover['продажи'], marker='o')
plt.title('Общий товарооборот')
plt.xlabel('Период')
plt.ylabel('Продажи')
plt.grid(True)
plt.tight_layout()
plt.show()

# Прогноз и визуализация по каждому товару
for product in df['товар'].unique():
    temp = df[df['товар'] == product].groupby('год-мес')['продажи'].sum().reset_index()

    #  дни с начала продаж
    temp['месяц_число'] = (temp['год-мес'] - temp['год-мес'].min()).dt.days
    X = temp[['месяц_число']]
    y = temp['продажи']
    model = LinearRegression().fit(X, y)

    # Прогноз на 3 месяца вперёд
    future_days = [X['месяц_число'].max() + i * 30 for i in range(1, 4)]
    future_preds = model.predict(pd.DataFrame({'месяц_число': future_days}))
    future_dates = pd.date_range(start=temp['год-мес'].max() + pd.DateOffset(months=1), periods=3, freq='MS')
    forecast_df = pd.DataFrame({'год-мес': future_dates, 'продажи': future_preds})

    # Объединение факта и прогноза
    combined = pd.concat([temp[['год-мес', 'продажи']], forecast_df])

    plt.figure(figsize=(10, 5))
    plt.plot(temp['год-мес'], temp['продажи'], label='Факт', marker='o')
    plt.plot(forecast_df['год-мес'], forecast_df['продажи'], label='Прогноз', linestyle='--', marker='x')
    plt.title(f'Прогноз продаж: {product}')
    plt.xlabel('Период')
    plt.ylabel('Продажи')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()