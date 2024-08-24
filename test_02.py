import pytest
from AT_02 import count_vowels

def test_all_vowels():
    """Проверка, что функция правильно считает гласные в строке, содержащей только гласные."""
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    """Проверка, что функция возвращает 0 для строки, не содержащей гласных."""
    assert count_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") == 0

def test_mixed_string():
    """Проверка, что функция правильно считает гласные в смешанных строках (включая прописные и строчные буквы)."""
    assert count_vowels("Hello, World!") == 3
    assert count_vowels("PyThOn PrOgRaMmInG") == 4
    assert count_vowels("12345!@#$%") == 0

if __name__ == "__main__":
    pytest.main()
