import os

from caesar import Caesar
from message import Message
from messages_prompts import *


VALID_ACTIONS = {'E': 'encrypt',
                 'D': 'decrypt',
                 'Q': 'quit'}
VALID_CIPHERS = [Caesar]


def clear_screen():
    os.system('clr' if os.name == 'nt' else 'clear')

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
        try:
            cipher_index = int(input(CIPHER_PROMPT_PART_2))
            if cipher_index <= len(VALID_CIPHERS):
                cipher = VALID_CIPHERS[cipher_index - 1]
                print(CIPHER_CONFIRMATION.format(cipher.__name__))
                return cipher
        except ValueError:
            pass

        print(CIPHER_INVALID_CHOICE)

def prompt_for_message(action):
    while True:
        message = Message(input(MESSAGE_PROMPT.format(action)))
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
        # Prompt for cipher **kwargs if needed
        # Prompt for pad and transform message if needed
        # Execute action on cipher
        # Prompt for output format and transform message if needed
        # Output message
