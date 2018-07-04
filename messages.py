import os
from messages_prompts import *


def clear_screen():
    os.system('clr' if os.name == 'nt' else 'clear')

def prompt_for_action():
    while True:
        action = input(ACTION_PROMPT)
        valid_actions = {'E': 'ENCRYPT',
                         'D': 'DECRYPT',
                         'Q': 'QUIT'
                         }
        if action.upper() in valid_actions.keys() or \
           action.upper() in valid_actions.values():
            return action.upper()[0]

        print(ACTION_INVALID_INPUT)


if __name__=='__main__':
    # Clear screen and print welcome message
    clear_screen()
    print(WELCOME)

    while True:
        # Prompt for action (encrypt, decrypt, quit)
        # If 'quit'
    	#     Print goodbye message and exit
        action = prompt_for_action()
        if action == 'Q':
            print(GOODBYE)
            break

        # Else
        # 	Prompt for message and transform message
        # 	Prompt for cipher and create cipher (validate input)
        # 	Prompt for cipher **kwargs if needed
        # 	Prompt for pad and transform message if needed
        # 	Execute action on cipher
        # 	Prompt for output format and transform message if needed
        # 	Output message
