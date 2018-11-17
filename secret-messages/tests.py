#!/usr/bin/env python3
import unittest
from secret_messages import (
    obfuscate,
    secret_translator,
    translate,
    translator
)


class TestSecretMessages(unittest.TestCase):
    """
    Tests assume you are using the default translator
    """

    def test_obfuscate_returns_secret_message(self):
        self.assertEqual(obfuscate('test', translator), '<%|<')

    def test_secret_translator(self):
        secret_code = secret_translator(translator)
        self.assertTrue('a' in secret_code.keys())

    def test_translate_returns_readable_message(self):
        self.assertEqual(translate('<%|<', translator), 'test')
