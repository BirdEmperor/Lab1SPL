# import unittest
# from Classes.calculator import Calculator

# class TestCalculator(unittest.TestCase):
    
#     def setUp(self):
#         self.calc = Calculator.calculate()

#     # Тестування додавання
#     def test_addition_positive_numbers(self):
#         self.calc.num1 = 5
#         self.calc.operator = '+'
#         self.calc.num2 = 3
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, 8)

#     def test_addition_negative_numbers(self):
#         self.calc.num1 = -5
#         self.calc.operator = '+'
#         self.calc.num2 = -3
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, -8)

#     def test_addition_mixed_numbers(self):
#         self.calc.num1 = -5
#         self.calc.operator = '+'
#         self.calc.num2 = 3
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, -2)

#     # Тестування віднімання
#     def test_subtraction_positive_numbers(self):
#         self.calc.num1 = 5
#         self.calc.operator = '-'
#         self.calc.num2 = 3
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, 2)

#     def test_subtraction_negative_result(self):
#         self.calc.num1 = 3
#         self.calc.operator = '-'
#         self.calc.num2 = 5
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, -2)

#     # Тестування множення
#     def test_multiplication_zero(self):
#         self.calc.num1 = 0
#         self.calc.operator = '*'
#         self.calc.num2 = 5
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, 0)

#     def test_multiplication_positive_numbers(self):
#         self.calc.num1 = 5
#         self.calc.operator = '*'
#         self.calc.num2 = 3
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, 15)

#     def test_multiplication_negative_numbers(self):
#         self.calc.num1 = -5
#         self.calc.operator = '*'
#         self.calc.num2 = -3
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, 15)

#     # Тестування ділення
#     def test_division_valid(self):
#         self.calc.num1 = 6
#         self.calc.operator = '/'
#         self.calc.num2 = 3
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, 2)

#     def test_division_by_zero(self):
#         self.calc.num1 = 5
#         self.calc.operator = '/'
#         self.calc.num2 = 0
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, "Помилка: ділення на нуль!")

#     # Тестування обробки помилок
#     def test_sqrt_negative(self):
#         self.calc.num1 = -4
#         self.calc.operator = '√'
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, "Помилка: корінь з від'ємного числа!")

#     def test_sqrt_positive(self):
#         self.calc.num1 = 9
#         self.calc.operator = '√'
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, 3)

# if __name__ == '__main__':
#     unittest.main()
