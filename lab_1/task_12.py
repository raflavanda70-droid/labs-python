BASE_COST = 24.99
BASE_MINUTES = 60
BASE_SMS = 30
BASE_INTERNET = 1024  # 1 ГБ = 1024 МБ
EXTRA_MINUTE_COST = 0.89
EXTRA_SMS_COST = 0.59
EXTRA_MB_COST = 0.79
TAX_RATE = 0.02  # 2%
used_minutes = int(input("Введите количество израсходованных минут: "))
used_sms = int(input("Введите количество израсходованных SMS: "))
used_internet = float(input("Введите количество израсходованного интернет-трафика (в МБ): "))
extra_minutes = max(0, used_minutes - BASE_MINUTES)
extra_sms = max(0, used_sms - BASE_SMS)
extra_internet = max(0, used_internet - BASE_INTERNET)
extra_minutes_cost = extra_minutes * EXTRA_MINUTE_COST
extra_sms_cost = extra_sms * EXTRA_SMS_COST
extra_internet_cost = extra_internet * EXTRA_MB_COST
subtotal = BASE_COST + extra_minutes_cost + extra_sms_cost + extra_internet_cost
tax = subtotal * TAX_RATE
total = subtotal + tax
print("\n--- Чек ---")
print(f"Базовая стоимость тарифа: {BASE_COST:.2f} руб.")
if extra_minutes > 0:
    print(f"Дополнительные минуты ({extra_minutes} мин.): {extra_minutes_cost:.2f} руб.")

if extra_sms > 0:
    print(f"Дополнительные SMS ({extra_sms} шт.): {extra_sms_cost:.2f} руб.")

if extra_internet > 0:
    print(f"Дополнительный интернет-трафик ({extra_internet:.2f} МБ): {extra_internet_cost:.2f} руб.")

print(f"Налог (2%): {tax:.2f} руб.")
print(f"Итоговая сумма к оплате: {total:.2f} руб.")