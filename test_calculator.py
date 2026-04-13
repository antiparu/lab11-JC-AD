#https://github.com/antiparu/lab11-JC-AD
#Josh Carrington as Partner 1
#Alejandro Delgado as Partner 2
import unittest
import calculator


class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self):
        self.assertEqual(calculator.add(3, 4), 7)
        self.assertEqual(calculator.add(-2, 5), 3)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(8, 2), 4)
        self.assertEqual(calculator.div(9, 3), 3)
        self.assertEqual(calculator.div(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10, 0)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)

    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(2, 8), 3)
        self.assertEqual(calculator.logarithm(10, 100), 2)
        self.assertEqual(calculator.logarithm(3, 27), 3)

    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 4), 8)
        self.assertEqual(calculator.mul(10, 0.5), 5)
        self.assertEqual(calculator.mul(4, -4), -16)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(16), 4)
        self.assertEqual(calculator.square_root(64), 8)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 3), 7)
        self.assertEqual(calculator.subtract(5, 10), -5)
        self.assertEqual(calculator.subtract(0, 0), 0)


if __name__ == "__main__":
    unittest.main()