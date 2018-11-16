import unittest
from unittest.mock import patch
from name import (
    get_name,
    movie_title,
    replace_letter,
    reverse_name
    )


class NameTest(unittest.TestCase):

    @patch('builtins.input', return_value='test')
    def test_get_name_returns_input(self, input):
        self.assertEqual(get_name(), 'test')

    @patch('builtins.input', return_value=None)
    def test_get_name_returns_default(self, input):
        self.assertEqual(get_name(), 'Pablo')

    def test_reverse_name_returns_reversed_string(self):
        self.assertEqual(reverse_name('Pablo'), 'olbaP')

    def test_replace_letter(self):
        self.assertEqual(replace_letter('Pablo', 'a', 'o'), 'Poblo')

    def test_movie_title(self):
        name = 'test'
        movie_titles = [
            f'{name} and me.'.title(),
            f'What about {name}.'.title(),
            f'{name} got her groove back.'.title(),
            f'The {name} show.'.title()
            ]
        self.assertTrue(movie_title(name) in movie_titles)
