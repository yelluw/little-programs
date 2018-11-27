#!/usr/bin/env python3

'''
Note:
(From same directory this file is in)
To run tests use 

python3 -m unittest
'''

import unittest
from unittest.mock import patch
from passwords import (
    ask_to_generate,
    ask_to_login,
    check_password_length,
    compare_password,
    get_password,
    random_password
)


class PasswordsTests(unittest.TestCase):

    @patch('builtins.input', return_value='y')
    def test_ask_to_generate_password_returns_user_input(self, user_input):
        self.assertEqual(ask_to_generate(), 'y')

    @patch('builtins.input', return_value='y')
    def test_ask_to_login_returns_user_input(self, user_input):
        self.assertEqual(ask_to_login(), 'y')

    def test_check_password_length_returns_true(self):
        self.assertTrue(check_password_length('ab', 'ab'))

    def test_check_password_length_returns_false(self):
        self.assertFalse(check_password_length('aab', 'ab'))

    def test_compare_password_returns_true(self):
        self.assertTrue(compare_password('ab', 'ab'))

    def test_compare_password_returns_false(self):
        self.assertFalse(compare_password('aab', 'ab'))

    @patch('builtins.input', return_value='ab')
    def test_get_password_returns_user_input(self, user_input):
        self.assertEqual(get_password(), 'ab')

    def test_random_password_returns_password_based_on_seed(self):
        self.assertTrue(random_password() in ['aa', 'ab', 'ba', 'bb'])
