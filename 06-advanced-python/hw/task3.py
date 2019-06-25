"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""
import string


class ShiftDescriptor:

    def __init__(self, shift):
        self.shift = shift
        self.value = ''

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[self.shift:] + alphabet[:self.shift]
        table = str.maketrans(alphabet, shifted_alphabet)
        self.value = value.translate(table)


class CeasarSipher:

    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)


a = CeasarSipher()
a.message = 'abc'
a.another_message = 'hello'
assert a.message == 'efg'
assert a.another_message == 'olssv'
