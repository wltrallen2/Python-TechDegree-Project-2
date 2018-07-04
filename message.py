import string

class Message(str):
    def __init__(self, text):
        self.text = self.transform_to_valid_format(text)

    def __str__(self):
        return self.text

    def transform_to_valid_format(self, text):
        new_text = ''
        for char in text:
            if char in string.ascii_letters:
                new_text += char.upper()
        return new_text

    def pad(self, pad_text):
        pass

    def group_characters(self, num_chars_per_group):
        pass
