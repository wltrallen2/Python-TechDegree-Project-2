################ USER MESSAGES & PROMPTS ################
# The following constants are listed alphabetically.
#########################################################


class Prompts:
    """This class provides static prompts for use in the main module
    for SECRET MESSAGES.
    """
    ACTION_INVALID_INPUT = '''
*** You've entered an invalid action. ***
Please enter [E]ncrypt, [D]ecrypt, or [Q]uit.'''

    ACTION_PROMPT = '''
Would you like to encrypt or decrypt a message?
(Type 'Q' or 'QUIT' to quit.) [E/D/Q] ==> '''

    CIPHER_CONFIRMATION = "\n*** You chose the {} Cipher. ***\n"

    CIPHER_INVALID_CHOICE = \
    "*** Oops! You didn't enter a valid numeric choice. ***\n"

    CIPHER_PROMPT_PART_1 = \
    "\nPlease choose the cipher you would like to use to {} your message:"

    CIPHER_PROMPT_PART_2 = "Enter the number of your choice here ==> "

    GOODBYE = '*** Thank you for using SECRET MESSAGES! ***\n\n\n'

    GROUP_INVALID = \
    """*** Oops! Please make a valid choice: [Y/N] ***"""

    GROUP_PROMPT = '''
Would you like to break the encrypted message
into five-character groups? [Y/N] '''

    KEYWORD_ARGS_INVALID = \
    "\n*** Oops! You didn't enter a valid {}. Please try again ==> "

    KEYWORD_ARGS_PROMPT = \
    "Please enter the following items for the {} cipher:"

    MESSAGE_PROMPT = \
    "Please enter the message you'd like to {}:\n"

    OUTPUT_PREMESSAGE = "\nHere is your {}ed message using the {} cipher: "

    PAD_CONFIRMATION = \
    "\nThe pad that will be used to {} this message is {}.\n"

    PAD_INVALID_LENGTH = '''
*** Remember that your pad must be the same number of character or more than
you original message, and it can only use upper case alphabetic letters. ***
'''

    PAD_PROMPT = '''
Please enter the one-time pad that you would like to use
to {} this message ==> '''

    USE_PAD_INVALID = \
    "*** Oops! Please make a valid choice: [Y/N] ***"

    USE_PAD_PROMPT = \
    "\nWould you like to use a one-time pad to {} this message? [Y/N] "

    WELCOME = \
'''Welcome to SECRET MESSAGES!

****************************************************************************
Please note that, for simplicity, SECRET MESSAGES will transform
all lower case letters into upper case and will ignore all
non-alphabetic characters including whitespace.
****************************************************************************
'''
