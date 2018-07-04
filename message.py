import string

class Message(str):
    def __init__(self, text):
        self.text = text
        self.transform_to_valid_format()

    def __str__(self):
        return self.text

    def transform_to_valid_format(self):
        new_text = ''
        for char in self.text:
            if char in string.ascii_letters or char == ' ':
                new_text += char.upper()
        self.text = new_text

    def pad(pad_text):
        pass

    def group_characters(num_chars_per_group):
        pass
