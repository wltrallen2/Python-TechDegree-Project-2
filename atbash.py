"""atbash.py encodes and decodes messages using the Atbash Cipher,
which maps each letter of the alphabet to its reverse. For example,
the 1st letter (A) is mapped to the last, or 26th letter, (Z), and
so on.

If the character is not one of the 26 letters of the alphabet,
it passes through the coding untouched. In other words, numbers and
symbols will appear in the coded or decoded messages as the same
numbers and symbols.
"""
from ciphers import Cipher
import string

ALPHABET = string.ascii_letters.upper()

class Atbash(Cipher):
    def encrypt(self, message):
        """encrypt(self, message) encrypts the <message> using
        the Atbash Cipher and returns the encoded message.
        """
        coded_message = ''
        for index in range(len(message)):
            letter = (message[index]).upper()
            if letter in ALPHABET:
                new_letter_index = len(ALPHABET) - ALPHABET.index(letter) - 1
                coded_message += ALPHABET[new_letter_index]
            else:
                coded_message += letter
        return coded_message

    def decrypt(self, message):
        """decrypt(self, message) decrypts the <message> using
        the Atbash Cipher and returns the decoded message.
        """
        return self.encrypt(message)
