def are_anagrams(word1, word2):

    word1_clean = word1.lower().replace(" ", "")
    word2_clean = word2.lower().replace(" ", "")

    return sorted(word1_clean) == sorted(word2_clean)


if __name__ == "__main__":
    w1 = input("Введите первое слово: ")
    w2 = input("Введите второе слово: ")

    if are_anagrams(w1, w2):
        print("True - слова являются анаграммами")
    else:
        print("False - слова не являются анаграммами")


import pytest

def test_are_anagrams_true():
    assert are_anagrams("listen", "silent") is True
    assert are_anagrams("evil", "vile") is True
    assert are_anagrams("python", "typhon") is True

def test_are_anagrams_false():
    assert are_anagrams("hello", "world") is False
    assert are_anagrams("test", "settle") is False

def test_are_anagrams_with_spaces():
    assert are_anagrams("rail safety", "fairy tales") is True
    assert are_anagrams("a gentleman", "elegant man") is True