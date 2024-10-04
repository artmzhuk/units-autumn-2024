import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertTrue(math.isinf(self.calculator.addition(math.inf, 1)))
        self.assertTrue(math.isnan(self.calculator.addition(math.nan, 1)))

    def test_subtract(self):
        self.assertEqual(self.calculator.subtraction(10, 5), 5)
        self.assertEqual(self.calculator.subtraction(0, 5), -5)
        self.assertEqual(self.calculator.subtraction(-5, -5), 0)
        self.assertTrue(math.isinf(self.calculator.subtraction(math.inf, 1)))
        self.assertTrue(math.isnan(self.calculator.subtraction(math.nan, 1)))

    def test_multiply(self):
        self.assertEqual(self.calculator.multiplication(3, 4), 12)
        self.assertEqual(self.calculator.multiplication(-3, 4), -12)
        self.assertEqual(self.calculator.multiplication(0, 100), 0)
        self.assertTrue(math.isinf(self.calculator.multiplication(math.inf, 1)))
        self.assertTrue(math.isnan(self.calculator.multiplication(math.nan, 1)))

    def test_divide(self):
        self.assertEqual(self.calculator.division(10, 2), 5)
        self.assertEqual(self.calculator.division(5, 1), 5)
        self.assertEqual(self.calculator.division(0, 1), 0)
        self.assertIsNone(self.calculator.division(5, 0))
        self.assertTrue(math.isinf(self.calculator.division(math.inf, 1)))
        self.assertTrue(math.isnan(self.calculator.division(1, math.nan)))

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-10), 10)
        self.assertEqual(self.calculator.absolute(10), 10)
        self.assertEqual(self.calculator.absolute(0), 0)
        self.assertTrue(math.isinf(self.calculator.absolute(math.inf)))
        self.assertTrue(math.isnan(self.calculator.absolute(math.nan)))

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(5, 0), 1)
        self.assertEqual(self.calculator.degree(-2, 2), 4)
        self.assertTrue(math.isinf(self.calculator.degree(math.inf, 2)))
        self.assertTrue(math.isnan(self.calculator.degree(math.nan, 2)))

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
        with self.assertRaises(ValueError):
            self.calculator.ln(0)
        self.assertTrue(math.isinf(self.calculator.ln(math.inf)))
        self.assertTrue(math.isnan(self.calculator.ln(math.nan)))

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)
        self.assertAlmostEqual(self.calculator.log(8, 2), 3)
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 10)
        self.assertTrue(math.isinf(self.calculator.log(math.inf, 10)))
        self.assertTrue(math.isnan(self.calculator.log(math.nan, 10)))

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(2), math.sqrt(2))
        self.assertTrue(math.isinf(self.calculator.sqrt(math.inf)))
        self.assertTrue(math.isnan(self.calculator.sqrt(math.nan)))

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(125, 3), 5)
        self.assertEqual(self.calculator.nth_root(16, 4), 2)
        self.assertTrue(math.isinf(self.calculator.nth_root(math.inf, 3)))
        self.assertTrue(math.isnan(self.calculator.nth_root(math.nan, 3)))


if __name__ == "__main__":
    unittest.main()
