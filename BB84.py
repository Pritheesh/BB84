import numpy as np


class Bob:
    def __init__(self, bases):
        self.bits = []
        self.bases = bases

    def __str__(self):
        return " Bits:   " + '  '.join(map(str, self.bits)) + "\n" + \
            "Bases:   " + '  '.join(map(str, self.bases)) + "\n"


class Alice:
    def __init__(self, bits, bases):
        self.bits = bits
        self.bases = bases
        self.polarized_state = self.encode()

    def __str__(self):
        return " Bits:  " + '  '.join(map(str, self.bits)) + "\n" + \
            "Bases: " + '  '.join(map(str, self.bases)) + "\n" + \
            "State: " + ' '.join(map(str, self.encoded)) + "\n"

    def encode(self):
        return [self._encode_(x, y) for x, y in zip(self.bits, self.bases)]

    def _encode_(self, bit, basis):
        if(bit == 0):
            return 0 if basis == 'r' else 45
        else:
            return 90 if basis == 'r' else 135


def initialize_alice(length):
    return Alice(generate_random_bits(length), generate_random_bases(length))


def initialize_bob(length):
    return Bob(generate_random_bases(length))


def generate_random_bits(length):
    return np.random.choice([0, 1], size=length)


def generate_random_bases(length):
    return np.random.choice(list("dr"), length)


def _measure_(state, basis):
    if state == 0:
        return if basis == "r" else
    elif state == 45:
        return _ if basis == "r" else _
    elif state == 90:
        return _ if basis == "r" else _
    else:
        return _ if basis == "r" else _
    pass


def measure(states, bases):
    return [_measure_(x, y) for x, y in zip(states, bases)]


alice = initialize_alice(10)
bob = initialize_bob(10)
print(alice)
print(bob)
