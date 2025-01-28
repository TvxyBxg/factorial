import unittest
from factorial import factorial  # Импортируем функцию из файла factorial.py
from unittest.mock import patch

class TestFactorial(unittest.TestCase):
    
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    @patch('builtins.input', side_effect=['5'])
    def test_user_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            number = int(input("Введите целое неотрицательное число для вычисления факториала: "))
            result = factorial(number)
            mock_print(f"Факториал числа {number} равен {result}")
            mock_print.assert_called_with("Факториал числа 5 равен 120")

if __name__ == '__main__':
    unittest.main()
