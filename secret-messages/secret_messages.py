#!/usr/bin/env python3

"""
Secret Messages is a little program
to share ideas with your friends
in a code others wont understand.
Similar to morse code.
Not secure!

Only works for text based files (not PDFs, Word, etc.)
"""

import os

# You can come up with your own secret code as well.
# Simply replace the keys with your own.
translator = {
    '!': 'a',
    '@': 'b',
    '#': 'c',
    '$': 'd',
    '%': 'e',
    '^': 'f',
    '&': 'g',
    '*': 'h',
    '(': 'i',
    ')': 'j',
    '-': 'k',
    'Å': 'l',
    '=': 'm',
    '~': 'n',
    '{': 'o',
    '}': 'p',
    '[': 'q',
    ']': 'r',
    '|': 's',
    '<': 't',
    '>': 'u',
    ':': 'v',
    ';': 'w',
    '_': 'x',
    'Ó': 'y',
    'Ç': 'z',
    '.': ' ',
    'Î': '.',
    'Ø': '\n'
} 

def secret_translator(translator):
    secret_code = {}
    for k,v in translator.items():
        secret_code.update({v: k})
    return secret_code

def read_message(filename):
    """
    Assumes file with secrets is
    in the same directory as this program
    """
    try:
        path = f'{os.path.abspath(os.path.dirname(__file__))}{os.sep}{filename}'
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print('I can\'t seem to find that file. Did you type its name correctly? Please, try again.')
        exit()

def write_message(message, filename):
    """
    Writes file with secrets
    in the same directory as this program
    """
    path = f'{os.path.abspath(os.path.dirname(__file__))}{os.sep}{filename}'
    with open(path, 'w') as f:
        return f.write(message)


def translate(secret_message, translator):
    translation = []
    for i in secret_message:
        letter = translator.get(i)
        if not letter:
            continue
        translation.append(letter)
    return ''.join(translation)

def obfuscate(message, translator):
    secret_code = secret_translator(translator)
    translation = []
    for i in message:
        code = secret_code.get(i, i)
        translation.append(code)
    return ''.join(translation)

def main():
    welcome_message = """
    Welcome to the secret message translator!
    Only share it with your friends... :)
    """
    choice = input('What do you want to do? Obfuscate or Translate? (type: o or t): ')
    if choice not in ['o', 't']:
        print('Sorry, that\'s not a valid option. Try again.  ')
        
    filename = input('What is the filename you want to use? : ')
    message = read_message(filename)
    
    translated_message = ''
    if choice == 'o':
        translated_message = obfuscate(message, translator)

    elif choice == 't':
        translated_message = translate(message, translator)    

    write_message(translated_message, filename)    

    print('Done!')

if __name__ == '__main__':
    main()
