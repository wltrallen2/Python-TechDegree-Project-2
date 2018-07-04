class Cipher:

    def __init__(self):
        self.arguments_dict = {}

    def __str__(self):
        return type(self).__name__

    def set_arguments(self):
        raise NotImplementedError()

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()
