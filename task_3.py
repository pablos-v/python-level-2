"""
Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
1 возврат строки без изменений
2 возврат строки с преобразованием регистра без потери символов
3 возврат строки с удалением знаков пунктуации
4 возврат строки с удалением букв других алфавитов
5 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

"""

import unittest

from task_1 import task_func


class TestTaskFunc(unittest.TestCase):
    def test_1(self):
        self.assertEqual(task_func('qwerty qwerty asd'), 'qwerty qwerty asd', msg='Failed test!')

    def test_2(self):
        self.assertEqual(task_func('qwerty qwERTY ASD'), 'qwerty qwerty asd', msg='Failed test!')

    def test_3(self):
        self.assertEqual(task_func('qwerty qw,..erty asd'), 'qwerty qwerty asd', msg='Failed test!')

    def test_4(self):
        self.assertEqual(task_func('qwйййerty qwысмкerty asd'), 'qwerty qwerty asd', msg='Failed test!')

    def test_5(self):
        self.assertEqual(task_func('qweваКПrty qWУУЦК-4466ERTy aSd'), 'qwerty qwerty asd', msg='Failed test!')


if __name__ == '__main__':
    unittest.main(verbosity=2)
