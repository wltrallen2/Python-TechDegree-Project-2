"""*********************************************************************
Manipulator (manipulator.py) contains four static levels meant to assist
with string manipulation when running SECRET MESSAGES (messages.py).

These four methods are as follows:
- transform_to_valid_format(text)
- pad(message, pad_text)
- unpad(message, pad_text)
- group_characters(message, num_chars_per_group)
*********************************************************************
"""

import random
import string

class Manipulator():
    def transform_to_valid_format(text):
        """Returns a string.

        Given a string (text), this function will strip
        all non-alphabetic characters including white space and transform
        the string into upper case before returning the new string value.
        """
        new_text = ''
        for char in text:
            if char in string.ascii_letters:
                new_text += char.upper()
        return new_text

    def pad(message, pad_text):
        """Returns a string to be used when encrypting a message.

        Given a two strings (message, pad_text), this function will add the
        values of corresponding letters in both strings, creating a new string
        based on the new values.

        For computational purposes,  'A' is equal to the value 0, 'B' is 1,
        'C' is 2, etc. For example, given 'CAT' and 'YAM', this function would
        perform the following operation:

        C + Y = 2 + 24 = 26 (-26) = 20 ==> A
        A + A = 0 + 0 = 0 = 0 ==> A
        T + M = 19 + 12 = 31 (-26) = 5 ==> F

        So, the return value would be AAF.
        """
        alphabet = string.ascii_letters.upper()

        padded_message = ''
        for char_index in range(len(message)):
            padded_char_index = alphabet.index(message[char_index]) \
                                + alphabet.index(pad_text[char_index])
            if padded_char_index > len(alphabet):
                padded_char_index - len(alphabet)
            padded_message += alphabet[padded_char_index]

        return padded_message

    def unpad(message, pad_text):
        """Returns a string to be used after decrypting a message.

        Given a two strings (message, pad_text), this function will find the
        difference between the values of corresponding letters in both strings,
        creating a new string based on the new values.

        For computational purposes,  'A' is equal to the value 0, 'B' is 1,
        'C' is 2, etc. For example, given 'AAF' and 'YAM', this function would
        perform the following operation:

        A - Y = 0 - 24 = -24 (+26) = 2 ==> C
        A - A = 0 - 0 = 0 = 0 ==> A
        F - M = 5 - 12 = -7 (+26) = 19 ==> T

        So, the return value would be CAT.
        """
        alphabet = string.ascii_letters.upper()

        unpadded_message = ''
        for char_index in range(len(message)):
            unpadded_char_index = alphabet.index(message[char_index]) \
                                - alphabet.index(pad_text[char_index])
            if unpadded_char_index < len(alphabet):
                unpadded_char_index + len(alphabet)
            unpadded_message += alphabet[unpadded_char_index]

        return unpadded_message

    def group_characters(message, num_chars_per_group):
        """Returns a string value formatted in groups of n characters with
        a single whitespace character between each group. This will also add
        punctuation or numerical characters to the output if the number of
        characters in the message variable is not evenly divisible by the
        number of characters per group.
        """
        #TODO: Add comments here to clarify algorithm.
        num_additional_chars = num_chars_per_group \
                               - (len(message) % num_chars_per_group)
        additional_chars = string.punctuation + string.digits
        for index in range(num_additional_chars):
            new_char = random.choice(additional_chars)
            new_char_index = int(random.uniform(0, len(message)))
            message = message[0:new_char_index] \
                      + new_char \
                      + message[new_char_index:]

        grouped_message = ''
        start_index = 0
        end_index = 0
        while end_index < len(message):
            end_index += 5
            grouped_message += message[start_index:end_index]
            start_index = end_index
            if start_index < len(message):
                grouped_message += ' '
        return grouped_message
