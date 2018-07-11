from .ciphers import Cipher


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Keyword(Cipher):
    """This class encodes and decodes messages using the Keyword Cipher,
    which creates a substitution cipher by removing each of the letters in a
    <keyword> (ignoring symbols, whitespace, and duplicate letters)
    from the English alphabet, then appending the <keyword> to the beginning
    of the alphabet. Next, a position-for-position substituion is made.

    If the character is not one of the 26 letters of the alphabet,
    it passes through the coding untouched. In other words, numbers and
    symbols will appear in the coded or decoded messages as the same
    numbers and symbols.
    """

    def __init__(self, key_word = ''):
        """The initializer accepts a keyword <key_word> and sets then
        instance variable <keyword_alphabet>. It also creates the
        <arguments_dict> variable which identifies that this class needs a
        'Key Word' argument that is passed in as a str object.
        """
        self.arguments_dict = {'Key Word': str}
        self.keyword_alphabet = self.__create_keyword_alphabet(key_word.upper())

    def set_arguments(self, new_args_dict):
        """This method sets the <keyword_alphabet> variable using the value
        that has been passed using the key 'Key Word' in the <arguments_dict>.
        The value should be a str object. The <keyword_alphabet> variable
        is the shifted alphabet that is used in the main substition cipher
        to both encrypt and decrypt messages.
        """
        self.keyword_alphabet = \
            self.__create_keyword_alphabet(new_args_dict['Key Word'].upper())

    def encrypt(self, message):
        """Returns the ecrypted message by substituting the letters
        in the standard alphabet with the letters in the class variable
        <keyword_alphabet>.
        """
        return self.__substitute_letters(message,
                                         ALPHABET,
                                         self.keyword_alphabet)

    def decrypt(self, message):
        """Returns the decrypted message by substituting the letters
        in the class variable <keyword_alphabet> with the letters in the
        standard alphabet.
        """
        return self.__substitute_letters(message,
                                         self.keyword_alphabet,
                                         ALPHABET)

    def __create_keyword_alphabet(self, key_word):
        """Returns a keyword_alphabet by removing the letters in the <key_word>
        from the English alphabet (ignoring symbols, whitespace, and duplicate
        letters), then appending the letters to the beginning of the remaining
        alphabet letters (again igoring symbols, whitespace, and duplicate
        letters).
        """
        keyword_push = ''
        keyword_alphabet = ALPHABET
        for letter in key_word:
            if letter in ALPHABET and letter not in keyword_push:
                keyword_push += letter
                keyword_alphabet = keyword_alphabet.replace(letter, '')
        keyword_alphabet = keyword_push + keyword_alphabet
        return keyword_alphabet

    def __substitute_letters(self, message, from_string, to_string):
        """Returns a string in which each letter is located in the
        from_string and replaced with the letter in the same index position
        in the to_string.
        """
        coded_message = ''
        for letter in message.upper():
            if letter in from_string:
                letter_index = from_string.index(letter)
                coded_message += to_string[letter_index]
            else:
                coded_message += letter
        return coded_message
