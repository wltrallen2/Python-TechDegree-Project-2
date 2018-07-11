from .ciphers import Cipher


class Transposition(Cipher):
    """This class encodes and decodes messages using the Rail Fence Cipher
    (a version of the Transposition cipher as defined at
    https://en.wikipedia.org/wiki/Transposition_cipher). The initializer
    requires an int that represents the number of rails to use, but
    it defaults to 3 if no int is passed.

    This version of Transposition requires that all characters be uppercase
    letters with no whitespace or other special characters.
    """
    def __init__(self, num_rails = 3):
        """The initializer accepts an int <num_rails> and sets then
        instance variable <num_rails>. If no int is passed, the initializer
        will set the default number of rails to 3.

        It also defines the arguments_dict variable to indicate that this
        cipher requires an int for the 'Number of Rails'.
        """
        super().__init__()
        self.arguments_dict = {'Number of Rails': int}

        if not(str(num_rails).isnumeric() and int(num_rails) > 1):
            num_rails = 3
        self.num_rails = int(num_rails)

    def set_arguments(self, args_dict):
        """Sets the number of rails to use in the enryption and decryption
        process by using the value that is attached to the key 'Number of
        Rails' in the arguments_dict.
        """
        self.num_rails = args_dict['Number of Rails']

    def encrypt(self, message):
        """Returns the ecrypted message using the Rail
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
                if self.__index_at_or_out_of_bounds(rail_index,
                                                    range(self.num_rails)):
                    rail_increment *= -1

        return ''.join(rails)

    def decrypt(self, message):
        """Returns the decrypted message using the Rail
        Fence Tranposition Cipher as described at
        https://en.wikipedia.org/wiki/Transposition_cipher.
        """
        coded_chars_list = list([''] * len(message))
        new_index = 0

        for rail_index in range(self.num_rails):
            ltr_index = rail_index
            alternating_factor = 'A'
            while ltr_index < len(message) and new_index < len(message):
                coded_chars_list[ltr_index] = message[new_index]
                new_index += 1
                ltr_index, alternating_factor = \
                    self.__get_next_index_for(ltr_index,
                                              self.num_rails,
                                              rail_index,
                                              alternating_factor)

        return ''.join(coded_chars_list)

    def __get_next_index_for(self, index, num_rails,
                             rail_index, alternating_factor):
        """Returns a tuple which includes an int value and an
        alternating_factor.

        The int value is used during the decryption process
        to determine the next index value (its position in the decoded message)
        for a letter in the encoded_message, which has been encoded using the
        Rail Fence Transposition Cipher.

        The alternating_factor is used in the algorithm to determine
        whether the message is travelling up or down the rails.
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

    def __index_at_or_out_of_bounds(self, index, range):
        """Returns True if the passed index is at or outside of the bounds
        of the given range. Otherwise, returns False.
        """
        if (index <= range.start) or (index >= range.stop - 1):
            return True
        return False
