import numpy as np

expenses = np.array([1500, 1400, 1600, 1700, 1800, 2000, 2100, 1900, 1700, 1600, 1500, 1700])

winter_months = [12, 1, 2]
summer_months = [6, 7, 8]
winter_indices = [month - 1 for month in winter_months]
summer_indices = [month - 1 for month in summer_months]

winter_total = np.sum(expenses[winter_indices])
summer_total = np.sum(expenses[summer_indices])

print(f"Зимние месяцы {winter_months}: {winter_total} руб.")
print(f"Летние месяцы {summer_months}: {summer_total} руб.")
print("Больше тратится в", "зимний" if winter_total > summer_total else "летний" if summer_total > winter_total else "оба периода одинаковы")

max_value = np.max(expenses)
max_months = np.where(expenses == max_value)[0] + 1
print(f"\nНаибольшие расходы в месяцах: {list(max_months)}")