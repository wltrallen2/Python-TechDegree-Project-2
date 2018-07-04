import string

class Manipulator():
    def transform_to_valid_format(text):
        new_text = ''
        for char in text:
            if char in string.ascii_letters:
                new_text += char.upper()
        return new_text

    def pad(message, pad_text):
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
        pass
