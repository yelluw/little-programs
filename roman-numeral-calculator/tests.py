import unittest
from roman_numeral_calculator import (
    value,
    substract,
    validate,
    calculate
)

class TestRomanNumeralCalcuator(unittest.TestCase):

    def test_value(self):
        self.assertEqual(value('V'), 5)

    def test_substract_returns_true(self):
        self.assertEqual(substract('IVV'), True)

    def test_substract_returns_false(self):
        self.assertEqual(substract('VVI'), False)

    def test_validate_returns_false_with_wrong_input_type(self):
        self.assertEqual(validate(1), False)

    def test_validate_returns_values_input_as_list(self):
        self.assertEqual(validate('VI'), ['V','I'])

    def test_calculate_does_addition(self):
        self.assertEqual(calculate('VI'), 6)

    def test_calculate_does_substraction(self):
        self.assertEqual(calculate('IV'), 4)
