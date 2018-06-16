'''*********************************************************************
messages.py encrypts or decrypts a message utilizing a user-selected
cipher from the following list:
   - Atbash Ciper,
   - Caesar Cipher,
   - Keyword Cipher, or
   - Transposition Cipher.

When encrypting, the user can also select the following options:
    - Output the code in five-letter blocks, or
    - Implement a one-time pad.
*********************************************************************
'''
import os
import random
import string
import textwrap
from atbash import Atbash
from caesar import Caesar
from keyword_cipher import Keyword
from transposition import Transposition


################ CONSTANTS ################
ENCRYPT = 'encrypt'
DECRYPT = 'decrypt'
QUIT = 'quit'
VALID_ACTIONS = {'e': ENCRYPT,
                 'd': DECRYPT,
                 'q': QUIT }

VALID_CIPHERS = [Atbash, Caesar, Keyword, Transposition]
REQUIRES_KEYWORD = [Keyword]
REQUIRES_KEY_NUMBER = [Transposition]

################ USER MESSAGES & PROMPTS ################
WELCOME = 'Welcome to Secret Messages!'

ACTION_PROMPT = '''
Would you like to encrypt or decrypt a message?
(Type 'Q' or 'QUIT' to quit.) [E/D/Q] ==> '''

INVALID_ACTION_MESSAGE = '''
You've entered an invalid action.
Please enter [E]ncrypt, [D]ecrypt, or [Q]uit.'''

CIPHER_PROMPT_PART_1 = '''
Please choose the cipher you would like to use to {} your message:'''

CIPHER_PROMPT_PART_2 = "Enter the number of your choice here ==> "

CIPHER_CONFIRMATION = "*** You chose the {} Cipher. ***\n"

CIPHER_PROMPT_ERROR_MESSAGE = \
"\n*** Oops! You didn't enter a valid numeric choice. ***\n"

MESSAGE_PROMPT = "Please enter the message you'd like to {}: \n"

DOES_USER_WANT_TO_PAD = \
"\nDo you want to use a one-time pad to {} your message? [Y/N] "

IS_TO_BE_RANDOM = \
"Do you want your pad to be generated randomly or would you like to \
\nenter the pad manually? [R]andom/[M]anually ==> "

ENTER_PADDED_MESSAGE = \
"\nPlease enter the pad for your message:\n"

ENTERED_INVALID_RESPONSE = \
"*** You've entered an invalid response. Please try again. ***\n"

PAD_REMINDER = \
'''*** Don't forget your pad. You will need it to decrypt the message. ***
Your pad is {}.'''

KEYWORD_PROMPT = \
"\nPlease enter the key word you'd like to use for this cipher ==> "

KEY_NUMBER_PROMPT = \
"\nPlease enter the key number you'd like to use for this cipher ==> "

INVALID_PAD = '''
*** The number of characters in your pad must match the number of characters
in your message. ***'''

OUTPUT_PREMESSAGE = "\nHere is your {}ed message using the {} cipher: "

EXIT_MESSAGE = '\nThank you for using Secret Messages!\n'


def clear_screen():
    """clear_screen() clears the screen for ease of readability."""
    os.system('clr' if os.name == 'nt' else 'clear')

def prompt_for_action():
    """prompt_for_action() uses a while True loop to display a user prompt,
    validate the input as part of either the keys or values of either
    VALID_ACTIONS constant, and return the user input.

    The loop will repeat until valid input has been provided.
    """
    while True:
        action = input(ACTION_PROMPT)
        action = action.lower()
        if action in VALID_ACTIONS.keys():
            action = VALID_ACTIONS[action]
        if action in VALID_ACTIONS.values():
            return action
        else:
            print(INVALID_ACTION_MESSAGE)

def prompt_for_cipher(action):
    """prompt_for_cipher(action) displays a list of available ciphers based on
    the constant VALID_CIPHERS, a list of available Cipher subclasses.
    Then, it prompts the user to choose a cipher to encrypt or decrypt
    the user message.
    """
    while True:
        print(CIPHER_PROMPT_PART_1.format(action))

        cipher_index = 1
        for valid_cipher in VALID_CIPHERS:
            print("     {}. {} Cipher"\
                    .format(cipher_index, valid_cipher.__name__))
            cipher_index += 1

        user_index = input(CIPHER_PROMPT_PART_2)
        try:
            cipher = VALID_CIPHERS[int(user_index) - 1]
            print(CIPHER_CONFIRMATION. format(cipher.__name__))
            return cipher
        except (ValueError, IndexError):
            print(CIPHER_PROMPT_ERROR_MESSAGE)

def prompt_for_message(action):
    """prompt_for_message(action) displays a prompt requesting the user to
    enter a message to be encrypted or decrypted utilizing the given
    action.
    """
    return input(MESSAGE_PROMPT.format(action))

def prompt_for_padding(action, message):
    while True:
        is_to_be_padded = (input(DOES_USER_WANT_TO_PAD.format(action))).upper()
        if is_to_be_padded in ['YES', 'Y']:
            is_to_be_random = input(IS_TO_BE_RANDOM).upper()
            if is_to_be_random in ['RANDOM', 'R']:
                padded_message = get_padded_message(message)
            elif is_to_be_random in ['MANUALLY', 'M']:
                pad = input(ENTER_PADDED_MESSAGE).upper()
                if len(pad) < len(message):
                    print(INVALID_PAD)
                    continue
                padded_message = get_padded_message(message, pad)
            else:
                print(INVALID_ACTION_MESSAGE)
                continue
        elif is_to_be_padded in ['NO', 'N']:
            padded_message = message
        else:
            print(ENTERED_INVALID_RESPONSE)
            continue

        print('PADDED MESSAGE: {}'.format(padded_message))
        return padded_message

def get_padded_message(message, pad = None):
    #TODO: Fix padded_message
    alphabet = string.ascii_uppercase
    if not pad:
        pad = ''.join(random.choice(alphabet) for i in range(len(message)))

    print(PAD_REMINDER.format(pad))
    padded_message = ''
    # import pdb; pdb.set_trace()
    for index in range(len(message)):
        letter = message[index]
        if letter.isalpha():
            shift = alphabet.index(pad[index])
            padded_message += shift_cap_letter(letter.upper(), shift)
    return padded_message

def shift_cap_letter(letter, shift):
    shifted_value = ord(letter) + shift
    if shifted_value > ord('Z'):
        shifted_value -= 26
    return chr(shifted_value)

def create_cipher_instance(cipher):
    """create_cipher_instance(cipher) returns a cipher instance
    of the correct type after propmtping for any necessary key
    words or numbers required by that type of cipher.
    """
    if cipher in REQUIRES_KEYWORD + REQUIRES_KEY_NUMBER:
        return cipher(get_key(cipher))
    return cipher()


def get_key(cipher):
    """get_key_word() prompts the user for a keyword for use in
    the cipher.
    """
    prompt = KEYWORD_PROMPT
    if cipher in REQUIRES_KEY_NUMBER:
        prompt = KEY_NUMBER_PROMPT

    return input(prompt)

def perform_action(action, cipher_instance, message):
    """perform_action(action, cipher, message) returns the user's message
    as an encrypted or decrypted string that has been coded using
    a subclass of the Cipher class.
    """
    if action == ENCRYPT:
        return cipher_instance.encrypt(message)
    else:
        return cipher_instance.decrypt(message)

def output_results(action, cipher, message):
    """output_results(action, message) outputs a user message reminding the
    user of the action taken and the name of the cipher used.
    Then, it prints the coded message.
    """
    print(OUTPUT_PREMESSAGE.format(action, cipher.__name__))
    print(message)


################ MAIN SCRIPT ################
if __name__ == "__main__":
    clear_screen()
    print(WELCOME)

    while True:
        action = prompt_for_action()
        if action == QUIT:
            print(EXIT_MESSAGE)
            break

        clear_screen()
        cipher = prompt_for_cipher(action)
        message = prompt_for_message(action)
        message = prompt_for_padding(action, message)
        cipher_instance = create_cipher_instance(cipher)
        coded_message = perform_action(action, cipher_instance, message)
        output_results(action, cipher, coded_message)
