import string

class Manipulator():
    def transform_to_valid_format(text):
        new_text = ''
        for char in text:
            if char in string.ascii_letters:
                new_text += char.upper()
        return new_text

    def pad(message, pad_text):
        pass

    def unpad(message, pad_text):
        pass

    def group_characters(message, num_chars_per_group):
        pass
