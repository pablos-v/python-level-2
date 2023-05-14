"""
Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

from string import ascii_letters
import pytest


def task_func(s: str) -> str:
    """
    Deleting from string s all symbols, witch are not space or a symbol of the latin alphabet.
    Returns clear string.
    >>> task_func('qwerty qwerty asd')
    'qwerty qwerty asd'
    >>> task_func('qwerty qwERTY ASD')
    'qwerty qwerty asd'
    >>> task_func('qwerty qw,..erty asd')
    'qwerty qwerty asd'
    >>> task_func('qwйййerty qwысмкerty asd')
    'qwerty qwerty asd'
    >>> task_func('qweваКПrty qWУУЦК-4466ERTy aSd')
    'qwerty qwerty asd'
    """
    res = ''.join(c for c in s if c in ascii_letters or c.isspace())
    return res.lower()


def test_no_changes():
    assert task_func('qwerty qwerty asd') == 'qwerty qwerty asd'


def test_register():
    assert task_func('qwerty qwERTY ASD') == 'qwerty qwerty asd'


def test_punctuation():
    assert task_func('qwerty qw,..erty asd') == 'qwerty qwerty asd'


def test_other_letters():
    assert task_func('qwйййerty qwысмкerty asd') == 'qwerty qwerty asd'


def test_every_issue():
    assert task_func('qweваКПrty qWУУЦК-4466ERTy aSd') == 'qwerty qwerty asd'


if __name__ == '__main__':
    pytest.main(['-v'])
