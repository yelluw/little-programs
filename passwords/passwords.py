#!/usr/bin/env python3
from random import choice


SEED = ('a', 'b')
DEFAULT_PASSWORD = 'ab'

error_message = 'Error. Please try again.'
generate_password_message = 'Do you want me to generate a password for you? (y/n)\n'
generated_password_messaged = 'Your new password is: {password}'
get_password_message = 'Please enter your password: '
login_question_message = 'Do you wish to login? (y/n)\n'
wrong_password_message = 'You entered the wrong password. Please try again.'
correct_password_meesage = 'You entered the correct password. You are now logged in.'
goodbye_message = 'GoodBye!'


def random_password(seed=SEED, length=2):
    return ''.join([choice(seed) for i in range(2)])


def check_password_length(input_password, stored_password):
    return len(input_password) == len(stored_password)


def compare_password(input_password, stored_password):
    return input_password == stored_password


def get_password():
    return input(get_password_message)


def ask_to_generate():
    return input(generate_password_message)


def ask_to_login():
    return input(login_question_message)


def main():
    generate = ask_to_generate()
    if generate == 'y':
        stored_password = random_password()
        print(generated_password_messaged.format(password=stored_password))
    
    elif generate == 'n':
        stored_password = DEFAULT_PASSWORD
    
    else:
        print(error_message)
        return 

    login = ask_to_login()
    if login != 'y':
        print(goodbye_message)
        return

    input_password = get_password()

    if all((check_password_length(input_password, stored_password), compare_password(input_password, stored_password))):
        print(correct_password_meesage)
    else:
        print(wrong_password_message)

    print(goodbye_message)


if __name__ == '__main__':
    main()
