import os
import string

from messages_prompts import *


VALID_ACTIONS = {'E': 'encrypt',
                 'D': 'decrypt',
                 'Q': 'quit'}


class Message(str):
    def __init__(self, text):
        self.text = text
        self.transform_to_valid_format()

    def __str__(self):
        return self.text

    def transform_to_valid_format(self):
        new_text = ''
        for char in self.text:
            if char in string.ascii_letters or char == ' ':
                new_text += char.upper()
        self.text = new_text

    def pad(pad_text):
        pass

    def group_characters(num_chars_per_group):
        pass


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

        # Prompt for message and transform message
        message = prompt_for_message(action)
        # Prompt for cipher and create cipher (validate input)
        # Prompt for cipher **kwargs if needed
        # Prompt for pad and transform message if needed
        # Execute action on cipher
        # Prompt for output format and transform message if needed
        # Output message
