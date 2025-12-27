word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

# Приводим слова к нижнему регистру и удаляем пробелы
word1_clean = word1.lower().replace(" ", "")
word2_clean = word2.lower().replace(" ", "")

# Проверяем, являются ли слова анаграммами
if sorted(word1_clean) == sorted(word2_clean):
    print("True - слова являются анаграммами")
else:
    print("False - слова не являются анаграммами")