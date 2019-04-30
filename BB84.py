import numpy as np

class Person:
    def __init__(self, bits, bases):
        self.bits = bits
        self.bases = bases
        self.encoded = self.encode()

    def __str__(self):
        return "Bits: " + ''.join(map(str, self.bits)) + "\n" + "Bases: " + ''.join(map(str, self.bases))

    def encode(self):
        return ""


def initialize(length):
    return Person(generate_random_bits(length), generate_random_bases(length))

def generate_random_bits(length):
    return np.random.choice([0,1], size=length)

def generate_random_bases(length):
    return np.random.choice(list("dr"), 100)

print(initialize(100))    
