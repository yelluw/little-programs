#!/usr/bin/env python3

"""
Hello!

This program asks for your name
and does some fun things with it.

Requires: Python 3.6 or higher.
"""
from random import randint

def get_name():
    name = input('Hi there! What is your name? ')
    if not name:
        # OK, dont want to give me your name.
        # I'll share mine.
        name = 'Pablo'
    return name

def reverse_name(name):
    # The [::-1] is a thing called extended slicing.
    # Look it up:
    # https://docs.python.org/3.6/whatsnew/2.3.html#extended-slices
    return name[::-1]

def replace_letter(name, letter, replacement):
    return name.replace(letter, replacement)

def movie_title(name):
    movie_titles = [
        f'{name} and me.',
        f'What about {name}.',
        f'{name} got her groove back.',
        f'The {name} show.'
    ]
    # selects a random title
    # and uppercases the words
    # https://docs.python.org/3.6/library/stdtypes.html?highlight=replace#str.title
    return movie_titles[randint(0, len(movie_titles))].title()

def main():
    name = get_name()
    
    print(reverse_name(name))

    # change the values of letter and replacement and see what happens
    letter = 'a'
    replacement = 'i'
    print(replace_letter(name, letter, replacement))
    
    print(movie_title(name))

if __name__ == '__main__':
    main()
