import string

class Cipher:
    def __init__(self, message, *args, **kwargs):
        self.message = message
        for item in kwargs:
            if kwargs[item]:
                item(message)

    def encrypt(self, message):
        if not self.uses_lowercase:
            message = message.upper()

        if not self.uses_special_chars:
            message = self._remove(message, string)

        if self.__name__ == 'Cipher':
            raise NotImplementedError()

    def decrypt(self, message):
        raise NotImplementedError()

    def pad (self, message, pad):
        raise NotImplementedError()

    def _validate(self, message):
        validated_string = ''
        invalidated_chars = ''
        for letter in message:
            if letter in string.printable:
                validated_string += letter
            else:
                invalidated_chars += letter
        if invalidated_chars != '':
            raise InvalidCharactersError()
        return validated_string

    def _remove(self, string, chars_to_remove):
        new_string = ''
        for letter in string:
            if letter not in chars_to_remove:
                new_string += letter
        return new_string

class InvalidCharactersError(BaseException):

    def __init__(self):
        super().__init__()
