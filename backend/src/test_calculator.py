import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative_and_positive(self):
        self.assertEqual(self.calculator.addition(-1, 1), 0)

    def test_add_zero(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_add_infinity(self):
        self.assertTrue(math.isinf(self.calculator.addition(math.inf, 1)))

    def test_add_nan(self):
        self.assertTrue(math.isnan(self.calculator.addition(math.nan, 1)))

    def test_add_float(self):
        self.assertEqual(self.calculator.addition(0.3, 0.25), 0.55)

    def test_add_float_int(self):
        self.assertEqual(self.calculator.addition(1.0, 2.0), 3.0)

    def test_add_zero_float(self):
        self.assertEqual(self.calculator.addition(0.0, 0.0), 0.0)

    def test_add_infinity_float(self):
        self.assertTrue(math.isinf(self.calculator.addition(math.inf, 1.1)))

    def test_add_nan_float(self):
        self.assertTrue(math.isnan(self.calculator.addition(math.nan, 1.1)))

    def test_add_string(self):
        self.assertEqual(self.calculator.addition("BMSTU", "1830"), "BMSTU1830")

    def test_add_string_empty(self):
        self.assertEqual(self.calculator.addition("BMSTU", ""), "BMSTU")

    def test_add_empty_string(self):
        self.assertEqual(self.calculator.addition("", "1830"), "1830")

    def test_add_invalid_string_and_int(self):
        with self.assertRaises(TypeError):
            self.calculator.addition("BMSTU", 1830)

    def test_subtract_positive(self):
        self.assertEqual(self.calculator.subtraction(10, 5), 5)

    def test_subtract_negative(self):
        self.assertEqual(self.calculator.subtraction(0, 5), -5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calculator.subtraction(-5, -5), 0)

    def test_subtract_infinity(self):
        self.assertTrue(math.isinf(self.calculator.subtraction(math.inf, 1)))

    def test_subtract_nan(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(math.nan, 1)))

    def test_subtract_float(self):
        self.assertEqual(self.calculator.subtraction(-5.2, -5.2), 0)

    def test_subtract_infinity_float(self):
        self.assertTrue(math.isinf(self.calculator.subtraction(math.inf, 1.1)))

    def test_subtract_nan_float(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(math.nan, 1.1)))

    def test_subtract_invalid_strings(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction("BMSTU", "STU")

    def test_multiply_integers(self):
        self.assertEqual(self.calculator.multiplication(3, 4), 12)

    def test_multiply_negative_positive(self):
        self.assertEqual(self.calculator.multiplication(-3, 4), -12)

    def test_multiply_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 100), 0)

    def test_multiply_infinity(self):
        self.assertTrue(math.isinf(self.calculator.multiplication(math.inf, 1)))

    def test_multiply_nan(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(math.nan, 1)))

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calculator.multiplication(-3.1, 4.2), -13.02)

    def test_multiply_zero_float(self):
        self.assertEqual(self.calculator.multiplication(0.0, 100.0), 0.0)

    def test_multiply_infinity_float(self):
        self.assertTrue(math.isinf(self.calculator.multiplication(math.inf, 1.5555)))

    def test_multiply_nan_float(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(math.nan, 1.666)))

    def test_multiply_string_repeat(self):
        self.assertEqual(self.calculator.multiplication("AH", 3), "AHAHAH")

    def test_multiply_int_string_repeat(self):
        self.assertEqual(self.calculator.multiplication(3, "AH"), "AHAHAH")

    def test_multiply_invalid_strings(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication("alpha", "beta")

    def test_divide_integers(self):
        self.assertEqual(self.calculator.division(10, 2), 5)

    def test_divide_by_one(self):
        self.assertEqual(self.calculator.division(5, 1), 5)

    def test_divide_zero_numerator(self):
        self.assertEqual(self.calculator.division(0, 1), 0)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calculator.division(5, 0))

    def test_divide_infinity(self):
        self.assertTrue(math.isinf(self.calculator.division(math.inf, 1)))

    def test_divide_nan(self):
        self.assertTrue(math.isnan(self.calculator.division(1, math.nan)))

    def test_divide_fraction(self):
        self.assertAlmostEqual(self.calculator.division(1, 3), 0.333333333333)

    def test_divide_float(self):
        self.assertEqual(self.calculator.division(10.5, 0.5), 21)

    def test_divide_invalid_strings(self):
        with self.assertRaises(TypeError):
            self.calculator.division("alpha", "beta")

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-10), 10)

    def test_absolute_positive(self):
        self.assertEqual(self.calculator.absolute(10), 10)

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_infinity(self):
        self.assertTrue(math.isinf(self.calculator.absolute(math.inf)))

    def test_absolute_nan(self):
        self.assertTrue(math.isnan(self.calculator.absolute(math.nan)))

    def test_absolute_float_positive(self):
        self.assertEqual(self.calculator.absolute(3.28), 3.28)

    def test_absolute_float_negative(self):
        self.assertEqual(self.calculator.absolute(-7.78), 7.78)

    def test_absolute_invalid_string(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute("alpha")

    def test_degree_positive(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_zero_exponent(self):
        self.assertEqual(self.calculator.degree(5, 0), 1)

    def test_degree_negative_base_even_exponent(self):
        self.assertEqual(self.calculator.degree(-2, 2), 4)

    def test_degree_infinity_base(self):
        self.assertTrue(math.isinf(self.calculator.degree(math.inf, 2)))

    def test_degree_nan_base(self):
        self.assertTrue(math.isnan(self.calculator.degree(math.nan, 2)))

    def test_degree_floats(self):
        self.assertEqual(self.calculator.degree(2.0, 2.0), 4.0)

    def test_degree_fraction_exponent(self):
        self.assertEqual(self.calculator.degree(4.0, 0.5), 2.0)

    def test_degree_invalid_string(self):
        with self.assertRaises(TypeError):
            self.calculator.degree("alpha", 2)

    def test_ln_one(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)

    def test_ln_e(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)

    def test_ln_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(0)

    def test_ln_infinity(self):
        self.assertTrue(math.isinf(self.calculator.ln(math.inf)))

    def test_ln_invalid_string(self):
        with self.assertRaises(TypeError):
            self.calculator.ln("alpha")

    def test_ln_nan(self):
        self.assertTrue(math.isnan(self.calculator.ln(math.nan)))

    def test_log_base_ten(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)

    def test_log_base_two(self):
        self.assertAlmostEqual(self.calculator.log(8, 2), 3)

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 10)

    def test_log_infinity(self):
        self.assertTrue(math.isinf(self.calculator.log(math.inf, 10)))

    def test_log_nan(self):
        self.assertTrue(math.isnan(self.calculator.log(math.nan, 10)))

    def test_log_invalid_string(self):
        with self.assertRaises(TypeError):
            self.calculator.log("alpha", 15)

    def test_sqrt_positive(self):
        self.assertEqual(self.calculator.sqrt(16), 4)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(2), math.sqrt(2))

    def test_sqrt_infinity(self):
        self.assertTrue(math.isinf(self.calculator.sqrt(math.inf)))

    def test_sqrt_nan(self):
        self.assertTrue(math.isnan(self.calculator.sqrt(math.nan)))

    def test_sqrt_fraction(self):
        self.assertEqual(self.calculator.sqrt(0.36), 0.6)

    def test_sqrt_invalid_string(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt("alpha")

    def test_nth_root_positive(self):
        self.assertAlmostEqual(self.calculator.nth_root(125, 3), 5)

    def test_nth_root_even_degree(self):
        self.assertEqual(self.calculator.nth_root(16, 4), 2)

    def test_nth_root_infinity(self):
        self.assertTrue(math.isinf(self.calculator.nth_root(math.inf, 3)))

    def test_nth_root_nan(self):
        self.assertTrue(math.isnan(self.calculator.nth_root(math.nan, 3)))

    def test_nth_root_fraction(self):
        self.assertAlmostEqual(self.calculator.nth_root(0.125, 3), 0.5)

    def test_nth_root_invalid_string(self):
        with self.assertRaises(TypeError):
            self.calculator.log("alpha", 5)


if __name__ == "__main__":
    unittest.main()
