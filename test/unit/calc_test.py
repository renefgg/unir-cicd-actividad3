import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)


    ########################## ACTIVIDAD 2 ###############################
    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(-4, self.calc.multiply(2, "-2"))
        self.assertEqual(0, self.calc.multiply(2, 0))
        self.assertEqual(6, self.calc.multiply("3", 2))

    def test_multiply_invalid_parameter_raises_value_error(self):
        self.assertRaises(TypeError, self.calc.multiply, "A", 0)
        self.assertRaises(TypeError, self.calc.multiply, 0, "B")

    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, "2"))
        self.assertEqual(9, self.calc.power(3, 2))
        self.assertEqual(16, self.calc.power("4", 2))
        self.assertEqual(1, self.calc.power(1, 0))

    def test_power_invalid_parameter_raises_value_error(self):
        self.assertRaises(TypeError, self.calc.power, "A", 0)
        self.assertRaises(TypeError, self.calc.power, 0, "B")

    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.sqrt(4))
        self.assertEqual(4, self.calc.sqrt(16))
        self.assertEqual(8, self.calc.sqrt("64"))
        self.assertEqual(10, self.calc.sqrt(100))

    def test_sqrt_invalid_parameter_raises_value_error(self):
        self.assertRaises(TypeError, self.calc.power, "A")

    def test_sqrt_negative_parameter_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)        

    def test_sqrt_invalid_parameter_raises_value_error(self):
        self.assertRaises(TypeError, self.calc.sqrt, "A")

    def test_log10_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(2, self.calc.log10(100))
        self.assertEqual(3, self.calc.log10(1000))

    def test_log10_invalid_parameter_raises_value_error(self):
        self.assertRaises(TypeError, self.calc.log10, "A")

    def test_log10_zero_parameter_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.calc.log10(0)
    #####################################################################

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
