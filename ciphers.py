class Cipher:

    def __init__(self, *arg, **kwargs):
        self.kwargs_keys = []

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()
