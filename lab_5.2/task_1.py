def count_words(sentence):
    words = sentence.strip().split()
    return len(words)

if __name__ == "__main__":
    user_input = input("Введите предложение: ")
    print("Количество слов:", count_words(user_input))

import pytest

def test_count_words_basic():
    assert count_words("Всем привет") == 2
    assert count_words("Это тестовое предложение") == 3

def test_count_words_empty():
    assert count_words("") == 0
    assert count_words("   ") == 0

def test_count_words_with_spaces():
    assert count_words("  пробелы  между   словами  ") == 3
    assert count_words("Начальный и конечный пробелы  ") == 4

def test_count_words_single_word():
    assert count_words("Слово") == 1
    assert count_words("  Слово  ") == 1