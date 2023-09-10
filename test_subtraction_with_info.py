import unittest
from Calculator import subtraction

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(subtraction(2, 3), -1)
        self.assertEqual(subtraction(-2, 3), -5)
        self.assertEqual(subtraction(-2, -3), 1)

if __name__ == '__main__':
    # Создаем набор тестов
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    
    # Запускаем тесты
    result = unittest.TextTestRunner().run(suite)
    
    # Выводим информацию о результатах
    print("\n")
    print("Tests Run:", result.testsRun)
    print("Errors:", len(result.errors))
    print("Failures:", len(result.failures))

    if result.wasSuccessful():
        print("All tests passed successfully!")
    else:
        print("Some tests failed.")
