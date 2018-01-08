import string
import random

class Cipher(object):
    def __init__(self, key=''.join(random.choice(string.ascii_lowercase) for _ in range(100))):
        if key.isalpha() and key.islower(): self.key = key
        else: raise ValueError("Incorrect input")

    def encode(self, text):
        encoded = []
        for t, k in zip(text, [ord(self.key[i % len(self.key)]) - 97 for i,v in enumerate(text)]):
            encoded.append(string.ascii_lowercase[(string.ascii_lowercase.index(t) + k) % 26])
        return "".join(encoded)

    def decode(self, text):
        decoded = []
        for t, k in zip(text, [ord(self.key[i % len(self.key)]) - 97 for i,v in enumerate(text)]):
            decoded.append(string.ascii_lowercase[(string.ascii_lowercase.index(t) - k) % 26])
        return "".join(decoded)

class Caesar(object):
    def encode(self, text):
        return Cipher("d").encode("".join([c.lower() for c in text if c.isalpha()]))

    def decode(self, text):
        return Cipher("d").decode(text)
