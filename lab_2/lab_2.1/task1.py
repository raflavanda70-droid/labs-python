text = input("Введите текст: ")

# Разбиваем текст на слова (игнорируем регистр)
words = text.lower().split()

word_count = {}

# Подсчитываем количество каждого слова
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\n1. Словарь с количеством  слов:")
for word, count in word_count.items():
    print("   '" + word + "': " + str(count))

unique_words_count = len(word_count)
print("\n2. Количество уникальных слов: " + str(unique_words_count))