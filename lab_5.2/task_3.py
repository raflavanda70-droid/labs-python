def is_palindrome(value):

    s = str(value)
    return s == s[::-1]


if __name__ == "__main__":
    user_input = input("Введите слово или число: ")
    if is_palindrome(user_input):
        print("палиндром ")
    else:
        print("не палиндром ")


import pytest

def test_is_palindrome_word():
    assert is_palindrome("level") is True
    assert is_palindrome("apple") is False

def test_is_palindrome_number():
    assert is_palindrome(121) is True
    assert is_palindrome(123) is False

def test_is_palindrome_empty():
    assert is_palindrome("") is True

def test_is_palindrome_case_sensitive():
    assert is_palindrome("Anna") is False
    assert is_palindrome("anna") is True