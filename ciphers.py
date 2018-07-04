class Cipher:

    def __init__(self):
        self.kwargs_keys = []

    def __str__(self):
        return type(self).__name__

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()
