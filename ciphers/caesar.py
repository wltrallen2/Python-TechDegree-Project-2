import string

from ciphers.ciphers import Cipher


class Caesar(Cipher):
    """This subclass of Cipher was provided by Team Treeshouse as an example
    of how subclassing should work for the 2nd project in the Python TechDegree
    program. Additional docstrings and comments were not added to this module.
    """
    FORWARD = string.ascii_uppercase * 3

    def __init__(self, offset=3):
        super().__init__()
        self.offset = offset
        self.FORWARD = string.ascii_uppercase + string.ascii_uppercase[:self.offset+1]
        self.BACKWARD = string.ascii_uppercase[:self.offset+1] + string.ascii_uppercase

    def encrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.FORWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.FORWARD[index+self.offset])
        return ''.join(output)

    def decrypt(self, text):
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.BACKWARD.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.BACKWARD[index-self.offset])
        return ''.join(output)
