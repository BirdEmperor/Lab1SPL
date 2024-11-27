# import unittest
# from Classes.calculator import Calculator
# from settings import decimal_places  # Импортируем настройки
# from __init__ import memory, history  # Память и история

# class TestCalculator(unittest.TestCase):

#     def setUp(self):
#         # Создаем экземпляр калькулятора
#         self.calc = Calculator()

#     # Тестирование сложения
#     def test_addition_positive_numbers(self):
#         self.calc.num1 = 5
#         self.calc.operator = '+'
#         self.calc.num2 = 3
#         self.calc.calculate()  # Вызываем расчет
#         self.calc.display_result()  # Отображаем результат
#         self.assertEqual(self.calc.result, 8)  # Проверяем результат

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

#     # Тестирование вычитания
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

#     # Тестирование умножения
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

#     # Тестирование деления
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
#         self.assertEqual(self.calc.result, "Ошибка: деление на ноль!")

#     # Тестирование обработки ошибок
#     def test_sqrt_negative(self):
#         self.calc.num1 = -4
#         self.calc.operator = '√'
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, "Ошибка: корень из отрицательного числа!")

#     def test_sqrt_positive(self):
#         self.calc.num1 = 9
#         self.calc.operator = '√'
#         self.calc.calculate()
#         self.calc.display_result()
#         self.assertEqual(self.calc.result, 3)

#     # Тестирование истории
#     def test_show_history(self):
#         # Имитация добавления операций в историю в раннере
#         self.calc.num1 = 5
#         self.calc.operator = '+'
#         self.calc.num2 = 3
#         self.calc.calculate()  # Вычисляем результат
#         self.calc.show_history()  # Показываем историю
#         self.assertIn("5 + 3 = 8", history)  # Проверяем, что результат в истории

#     # Тестирование памяти
#     def test_memory_storage(self):
#         # Имитация добавления в память
#         self.calc.num1 = 5
#         self.calc.operator = '+'
#         self.calc.num2 = 3
#         self.calc.calculate()  # Вычисляем результат
#         self.assertIn(self.calc.result, memory)  # Проверяем, что результат в памяти

# if __name__ == '__main__':
#     unittest.main()
