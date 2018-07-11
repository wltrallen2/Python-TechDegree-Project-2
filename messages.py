'''*********************************************************************
SECRET MESSAGES (messages.py) encrypts or decrypts a message utilizing
a user-selected cipher from the following list:
   - Atbash Ciper,
   - Caesar Cipher,
   - Keyword Cipher, or
   - Transposition Cipher.

When encrypting, the user can also select the following options:
    - Output the code in five-letter blocks, or
    - Implement a one-time pad.

When decrypting, if the message was encrypted using a one-time pad,
the user must enter the pad to correctly decrpyt the message.

This program will strip any message of non-alphabetic characters (including
whitespace) and transform all characters to upper case.
*********************************************************************
'''

import os

from ciphers.atbash import Atbash
from ciphers.caesar import Caesar
from ciphers.keyword_cipher import Keyword
from ciphers.transposition import Transposition

from utilities.manipulator import Manipulator
from utilities.messages_prompts import *


########## CONSTANTS ##########
VALID_ACTIONS = {'E': 'encrypt',
                 'D': 'decrypt',
                 'Q': 'quit'}
VALID_CIPHERS = [Atbash, Caesar, Keyword, Transposition]


################# HELPER FUNCTIONS ##################
# These helper functions are listed alphabetically. #
#####################################################
def clear_screen():
    """Clears the screen to increase readability."""
    os.system('clr' if os.name == 'nt' else 'clear')

def execute_action(action, cipher, message):
    """Given the action ('encrypt' or 'decrypt'), this function will
    return the encrypted or decrypted message using the given cipher.
    """
    if action == 'encrypt':
        return cipher.encrypt(message)
    return cipher.decrypt(message)

def prompt_for_action():
    """Returns a string value in lower case from the following list:
    ['encrypt', 'decrypt', 'quit'].

    This function will prompt the user to choose one of three options.
    If the input is invalid, the function will loop until valid input is
    entered. Users may enter upper or lower case or may use just the first
    character of the desired choice.
    """
    while True:
        action = input(ACTION_PROMPT).upper()
        if action in VALID_ACTIONS.keys():
            return VALID_ACTIONS[action]
        if action.lower() in VALID_ACTIONS.values():
            return action.lower()

        print(ACTION_INVALID_INPUT)

def prompt_for_cipher(action):
    """Returns an instance of a Cipher subclass.

    This function will prompt the user to choose one of the valid ciphers.
    The ciphers will be read in based on the VALID_CIPHERS constant, which
    should be a list of subclasses of Cipher. Users choose one of the valid
    ciphers by entering in the corresponding line item number as printed
    on the screen. If the input is invalid, the function will loop until
    valid input is entered.
    """
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
    """This function will prompt the user to enter any arguments that are
    necessary to use the chosen cipher. (For example, the transposition cipher
    requires the 'Number of Rails' that the encryptor should use.)

    The function does this by checking for an arguments_dict in the Cipher
    subclass, and if it finds one, iterates through the keys, querying
    the user for each key.

    If the user input does not match the dictionary value (a class type),
    the function will continue to loop until valid input is provided.

    Once all arguments have been provided, the function calls the Cipher
    subclass's method set_arguments(arguments_dict) to set each argument.

    If the argument_dict is empty, the function completes without making any
    changes.
    """
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
    """Returns a string value based on the user input and string manipulation
    as described below.

    This function prompts the user to enter the message that they would
    like to have encrypted or decrypted. Then, it runs the user input through
    a filter to strip away any non-alphabetic characters including whitespace,
    and to transform the message into uppercase.
    """
    message = input(MESSAGE_PROMPT.format(action))
    message = Manipulator.transform_to_valid_format(message)
    return message

def prompt_for_output_format(message):
    """Returns a string value representing the message formatted to user
    specifications:

    The user can choose to have their output separated into groups of five
    (5) characters, each separated by a single whitespace, or to have their
    output returned as one long string without whitespace.
    """
    while True:
        use_output = input(GROUP_PROMPT).upper()
        if use_output in ['Y', 'YES']:
            message = Manipulator.group_characters(message, 5)
        elif use_output not in ['N', 'NO']:
            print(GROUP_INVALID)
            continue
        return message

def prompt_for_pad(action, message):
    """Returns a string that respresents the one-time pad to be used
    to encrypt or decrypt the message. The pad will have been stripped of all
    non-alphabetic characters including whitespace, and will be in all
    uppercase.

    If the user decides not to use a one-time pad, an empty string is returned.

    If the user enters invalid input at either prompt contained within this
    function, the function will loop until valid input is provided.
    """
    pad = ''
    while True:
        use_pad = input(USE_PAD_PROMPT.format(action))
        if use_pad.upper() not in {'Y': 'YES', 'N': 'NO'}:
            print(USE_PAD_INVALID)
            continue
        elif use_pad.upper() in {'Y', 'YES'}:
            while pad == '':
                new_pad = input(PAD_PROMPT.format(action))
                new_pad = Manipulator.transform_to_valid_format(new_pad)
                if len(new_pad) < len(message):
                    print(PAD_INVALID_LENGTH)
                    continue
                print(PAD_CONFIRMATION.format(action, new_pad))
                pad = new_pad
        break
    return pad


################# __MAIN__ METHOD ##################
####################################################
if __name__=='__main__':
    clear_screen()
    print(WELCOME)

    # This is the beginning of the primary control loop, which will loop
    # until the user enters 'Q' or 'Quit' at the action_prompt.
    while True:
        action = prompt_for_action()
        clear_screen()
        if action == 'quit':
            print(GOODBYE)
            break

        # The following code prompts the user to enter the message,
        # choose a cipher, and enter and arguments required by the chosen
        # cipher.
        message = prompt_for_message(action)
        cipher = prompt_for_cipher(action)
        prompt_for_cipher_kwargs(cipher)

        # The following code allows the user to choose to use a one-time
        # pad. Then, if encrypting, it transforms the message using the pad
        # and encrypts the message. If decrypting, it decrypts the message,
        # then transforms the decryption using the pad.
        pad = prompt_for_pad(action, message)
        if pad != '' and action == 'encrypt':
            message = Manipulator.pad(message, pad)
        message = execute_action(action, cipher, message)
        if pad != '' and action == 'decrypt':
            message = Manipulator.unpad(message, pad)

        # If encrypting, the following code will prompt the user to choose
        # whether to break up the output into five-character segments.
        if action == 'encrypt':
            message = prompt_for_output_format(message)

        # Finally, the following code outputs the message.
        print(OUTPUT_PREMESSAGE.format(action, cipher))
        print(message)
