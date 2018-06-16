"""transposition.py encodes and decodes messages using the Rail Fence Cipher
(a version of the Transposition cipher as defined at
https://en.wikipedia.org/wiki/Transposition_cipher). The initializer
requires an int that represents the number of rails to use, but
it defaults to 3 if no int is passed.

If the character is not one of the 26 letters of the alphabet,
it is ignored and not included in the returned value. In other words,
numbers, symbols, and white space are excluded from the code.
"""

from ciphers import Cipher

class Transposition(Cipher):
    def __init__(self, num_rails = 3):
        """The initializer accepts a an int <num_rails> and sets then
        instance variable <num_rails>.
        """
        if not(num_rails.isnumeric() and int(num_rails) > 1):
            num_rails = 3
        self.num_rails = int(num_rails)

    def encrypt(self, message):
        """encrypt(message) encrypts the <message> using the Rail
        Fence Tranposition Cipher as described at
        https://en.wikipedia.org/wiki/Transposition_cipher.
        """
        rails = [''] * self.num_rails
        rail_increment = 1
        rail_index = 0

        for letter in message:
            if letter.isalpha():
                rails[rail_index] += letter.upper()
                rail_index += rail_increment
                if index_at_or_out_of_bounds(rail_index, range(self.num_rails)):
                    rail_increment *= -1

        return ''.join(rails)

    def decrypt(self, message):
        """decrypt(message) decrypts the <message> using the Rail
        Fence Tranposition Cipher as described at
        https://en.wikipedia.org/wiki/Transposition_cipher.
        """
        message = remove_non_alpha_chars(message)
        coded_chars_list = list([''] * len(message))
        new_index = 0

        for rail_index in range(self.num_rails):
            ltr_index = rail_index
            alternating_factor = 'A'
            while ltr_index < len(message) and new_index < len(message):
                coded_chars_list[ltr_index] = message[new_index]
                new_index += 1
                ltr_index, alternating_factor = \
                    get_next_index_for(ltr_index,
                                       self.num_rails,
                                       rail_index,
                                       alternating_factor)

        return ''.join(coded_chars_list)


def get_next_index_for(index, num_rails, rail_index, alternating_factor):
    """This is a helper function is used during the decryption process
    to determine the next index value (its position in the decoded message)
    for a letter in the encoded_message, which has been encoded using the
    Rail Fence Transposition Cipher.
    """
    if rail_index == num_rails - 1:
        rail_index = 0

    increment = (2 * num_rails) - (2 * rail_index) - 2
    if rail_index == 0:
        return index + increment, 'A'
    elif alternating_factor == 'A':
        return index + increment, 'B'
    else:
        increment = (2 * rail_index)
        return index + increment, 'A'

def index_at_or_out_of_bounds(index, range):
    """This is a helper function that helps to determine if the passed
    index is at or outside of the bounds of the given range.
    """
    if (index <= range.start) or (index >= range.stop - 1):
        return True

def remove_non_alpha_chars(message):
    """This is a helper function that removes the non-alphabetic
    characters from a passed string and returns the mutated string.
    """
    for char in message:
        if not char.isalpha():
            message = message.replace(char, '')
    return message
