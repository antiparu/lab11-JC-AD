import unittest
import calculator

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self):
        self.assertEqual(calculator.add(3, 4), 7)
        self.assertEqual(calculator.add(-2, 5), 3)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.sub(10, 3), 7)
        self.assertEqual(calculator.sub(5, 10), -5)
        self.assertEqual(calculator.sub(0, 0), 0)
    ##########################

    ######## Partner 1
    # def test_multiply(self):
    #     fill in code

    # def test_divide(self):
    #     fill in code
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_logarithm(self):
        self.assertEqual(calculator.log(2, 8), 3)
        self.assertEqual(calculator.log(10, 100), 2)
        self.assertEqual(calculator.log(3, 27), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(1, 10)
        with self.assertRaises(ValueError):
            calculator.log(-2, 10)
        with self.assertRaises(ValueError):
            calculator.log(2, -5)
    ##########################

    ######## Partner 1
    # def test_log_invalid_argument(self):
    #     fill in code

    # def test_hypotenuse(self):
    #     fill in code

    # def test_sqrt(self):
    #     fill in code
    ##########################

if __name__ == "__main__":
    unittest.main()