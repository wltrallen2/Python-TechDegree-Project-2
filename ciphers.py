class Cipher:
    """Subclasses of Cipher that require special arguments in order to
    encrypt or decrypt a message should override the __init__() method to
    include an arguments_dict that uses a description of the argument as the
    key and the argument type (e.g. str, int) as the argument value. These
    subclasses should also override the set_arguments function to ensure
    that each arguments value is stored appropriately in the Cipher subclass
    instance.

    All sublcasses of Cipher should also override the following two methods:
    - encrypt()
    - decrypt()

    If there are no arguments that need to be set, set_arguments() can simply
    pass
    """

    def __init__(self):
        """Initializes a Cipher instance by setting the local variable
        arguments_dict to an empty dictionary.
        """
        self.arguments_dict = {}

    def __str__(self):
        """Returns the name of the class (or subclass).
        """
        return type(self).__name__

    def set_arguments(self):
        """This function must be implemented for all subclasses of Cipher
        that require additional arguments in order to encrypt or decrypt a
        message.
        """
        raise NotImplementedError()

    def encrypt(self):
        """This function must be implemented for all subclasses of Cipher.
        """
        raise NotImplementedError()

    def decrypt(self):
        """This function must be implemented for all subclasses of Cipher.
        """
        raise NotImplementedError()
