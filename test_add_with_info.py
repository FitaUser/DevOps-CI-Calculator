import unittest
from Calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-2, -3), -5)

if __name__ == '__main__':
    # test complex
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    
    # Run tests
    result = unittest.TextTestRunner().run(suite)
    
    # Print result
    print("\n")
    print("Tests Run:", result.testsRun)
    print("Errors:", len(result.errors))
    print("Failures:", len(result.failures))

    if result.wasSuccessful():
        print("All tests passed successfully!")
    else:
        print("Some tests failed.")
