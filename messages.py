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
import textwrap
from caesar import Caesar


################ CONSTANTS ################
ENCRYPT = 'encrypt'
DECRYPT = 'decrypt'
QUIT = 'quit'
VALID_ACTIONS = {'e': ENCRYPT,
                 'd': DECRYPT,
                 'q': QUIT }

VALID_CIPHERS = [Caesar]
REQUIRES_KEYWORD = []
REQUIRES_KEY_NUMBER = []

################ USER MESSAGES & PROMPTS ################
ACTION_PROMPT = '''
Would you like to encrypt or decrypt a message?
(Type 'Q' or 'QUIT' to quit.) [E/D/Q] ==> '''

CIPHER_CONFIRMATION = "*** You chose the {} Cipher. ***\n"

CIPHER_PROMPT_ERROR_MESSAGE = \
"\n*** Oops! You didn't enter a valid numeric choice. ***\n"

CIPHER_PROMPT_PART_1 = "Please choose the cipher you would like to use to {} \
your message:"

CIPHER_PROMPT_PART_2 = "Enter the number of your choice here ==> "

EXIT_MESSAGE = '\nThank you for using Secret Messages!\n'

INVALID_ACTION_MESSAGE = '''
You've entered an invalid action.
Please enter [E]ncrypt, [D]ecrypt, or [Q]uit.'''

KEY_NUMBER_PROMPT = \
"\nPlease enter the key number you'd like to use for this cipher ==> "

KEYWORD_PROMPT = \
"\nPlease enter the key word you'd like to use for this cipher ==> "

MESSAGE_PROMPT = "Please enter the message you'd like to {}: \n"

OUTPUT_PREMESSAGE = "\nHere is your {}ed message using the {} cipher: "

WELCOME = 'Welcome to Secret Messages!'


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
        cipher_instance = create_cipher_instance(cipher)
        coded_message = perform_action(action, cipher_instance, message)
        output_results(action, cipher, coded_message)
