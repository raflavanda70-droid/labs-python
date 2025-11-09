import pandas as pd
import numpy as np
from faker import Faker
import matplotlib.pyplot as plt
import seaborn as sns

fake = Faker('ru_RU')
np.random.seed(42)

years = [2021, 2022, 2023, 2024, 2025]
subjects = ['Математика', 'Белорусский  язык', 'Физика', 'Химия', 'Биология']
specialties = ['Информатика', 'Физика', 'Химия', 'Биология', 'Математика']
forms = ['Очная', 'Заочная']

data = []
for year in years:
    for _ in range(100):
        student = {
            'ФИО': fake.name(),
            'Год поступления': year,
            'Форма обучения': np.random.choice(forms),
            'Средний балл аттестата': round(np.random.uniform(4.0, 10.0), 1),
            'Специальность': np.random.choice(specialties),
            'Адрес': fake.address().replace('\n', ', '),
            'Телефон': fake.phone_number()
        }

        ct_scores = {}
        for subject in subjects:
            base_score = np.random.normal(50 + (year - 2021) * 3, 12)
            ct_scores[f'ЦЭ/ЦТ_{subject}'] = max(0, min(100, int(base_score)))

        student.update(ct_scores)

        best_scores = sorted([ct_scores[f'ЦЭ/ЦТ_{sub}'] for sub in subjects], reverse=True)[:3]
        student['Общий балл'] = sum(best_scores) + student['Средний балл аттестата']

        data.append(student)

df = pd.DataFrame(data)

fig, axes = plt.subplots(3, 2, figsize=(15, 12))

ct_columns = [f'ЦЭ/ЦТ_{sub}' for sub in subjects]
ct_means = df.groupby('Год поступления')[ct_columns].mean()
ct_means.plot(ax=axes[0, 0], marker='o', linewidth=2)
axes[0, 0].set_title('Динамика среднего балла ЦТ по предметам')
axes[0, 0].set_ylabel('Средний балл')
axes[0, 0].grid(True)

cert_mean = df.groupby('Год поступления')['Средний балл аттестата'].mean()
axes[0, 1].plot(cert_mean.index, cert_mean.values, marker='s', linewidth=3, color='red')
axes[0, 1].set_title('Динамика среднего балла аттестата')
axes[0, 1].set_ylabel('Средний балл')
axes[0, 1].grid(True)

passing_scores = df.groupby(['Год поступления', 'Специальность'])['Общий балл'].min().unstack()
passing_scores.plot(ax=axes[1, 0], marker='o', linewidth=2)
axes[1, 0].set_title('Динамика проходного балла по специальностям')
axes[1, 0].set_ylabel('Проходной балл')
axes[1, 0].grid(True)

specialty_counts = df['Специальность'].value_counts()
axes[1, 1].bar(specialty_counts.index, specialty_counts.values, color='skyblue')
axes[1, 1].set_title('Количество поступивших по специальностям')
axes[1, 1].set_ylabel('Количество студентов')
plt.setp(axes[1, 1].xaxis.get_majorticklabels(), rotation=45)

form_stats = df['Форма обучения'].value_counts()
axes[2, 0].pie(form_stats.values, labels=form_stats.index, autopct='%1.1f%%', startangle=90)
axes[2, 0].set_title('Распределение по формам обучения')

axes[2, 1].set_visible(False)

plt.tight_layout()
plt.show()

print("Первые 5 записей данных:")
print(df.head())

print(f"\nОбщее количество студентов: {len(df)}")
print(f"Годы: {years}")
print(f"Специальности: {specialties}")