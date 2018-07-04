import os

from atbash import Atbash
from caesar import Caesar
from keyword_cipher import Keyword
from transposition import Transposition

from manipulator import Manipulator
from messages_prompts import *


VALID_ACTIONS = {'E': 'encrypt',
                 'D': 'decrypt',
                 'Q': 'quit'}
VALID_CIPHERS = [Atbash, Caesar, Keyword, Transposition]


def clear_screen():
    os.system('clr' if os.name == 'nt' else 'clear')

def execute_action(action, cipher, message):
    if action == 'encrypt':
        return cipher.encrypt(message)
    return cipher.decrypt(message)

def prompt_for_action():
    while True:
        action = input(ACTION_PROMPT).upper()
        if action in VALID_ACTIONS.keys():
            return VALID_ACTIONS[action]
        if action.lower() in VALID_ACTIONS.values():
            return action.lower()

        print(ACTION_INVALID_INPUT)

def prompt_for_cipher(action):
    while True:
        print(CIPHER_PROMPT_PART_1.format(action))
        cipher_i = 1
        for cipher_class in VALID_CIPHERS:
            print('{}: {}'.format(cipher_i, cipher_class.__name__))
            cipher_i += 1
        try:
            cipher_index = int(input(CIPHER_PROMPT_PART_2))
            if cipher_index <= len(VALID_CIPHERS):
                cipher = VALID_CIPHERS[cipher_index - 1]
                print(CIPHER_CONFIRMATION.format(cipher.__name__))
                return cipher()
        except ValueError:
            # Invalid input (whether alphabetic or out-of-range numeric)
            # is referenced in the print statement below.
            pass

        print(CIPHER_INVALID_CHOICE)

def prompt_for_cipher_kwargs(cipher):
    if cipher.arguments_dict != {}:
        new_args_dict = {}
        print(KEYWORD_ARGS_PROMPT.format(cipher))
        for args_key in cipher.arguments_dict:
            valid_keyword = False
            while not valid_keyword:
                value = input('{} ==> '. format(args_key))
                req_cls = cipher.arguments_dict[args_key]
                try:
                    value = req_cls(value)
                except ValueError:
                    print(KEYWORD_ARGS_INVALID.format(req_cls.__name__))
                    continue
                new_args_dict[args_key] = value
                break
        cipher.set_arguments(new_args_dict)

def prompt_for_message(action):
    while True:
        message = input(MESSAGE_PROMPT.format(action))
        message = Manipulator.transform_to_valid_format(message)
        return message
        break


if __name__=='__main__':
    clear_screen()
    print(WELCOME)

    while True:
        action = prompt_for_action()
        if action == 'quit':
            print(GOODBYE)
            break

        message = prompt_for_message(action)
        cipher = prompt_for_cipher(action)
        prompt_for_cipher_kwargs(cipher)
        # Prompt for pad and transform message if needed
        # Execute action on cipher
        message = execute_action(action, cipher, message)
        # Prompt for output format and transform message if needed
        print(OUTPUT_PREMESSAGE.format(action, cipher))
        print(message)
