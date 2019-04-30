import numpy as np


class Bob:
    def __init__(self, bases):
        self.bits = []
        self.bases = bases
        self.photons = []
        self.measured = False

    def __str__(self):
        return " Bits:   " + '  '.join(map(str, self.bits)) + "\n" + \
            "Bases:   " + '  '.join(map(str, self.bases)) + "\n"

    def measure(self, states, bases):
        self.measured = True
        self.photons = [self._measure(x, y) for x, y in zip(states, bases)]

    def _measure(self, state, basis):
        if basis == "r":
            if state in [0, 90]:
                return state
            else:
                return np.random.choice([0, 90])
        else:
            if state in [45, 135]:
                return state
            else:
                return np.random.choice([45, 135])

    def decode(self):
        if self.measured:
            self.bits = [1 if x == 90 or x == 135  else 0 for x in self.photons]
        else:
            raise Exception("Not measured to decode.")
        pass



class Alice:
    def __init__(self, bits, bases):
        self.bits = bits
        self.bases = bases
        self.photons = self.encode()

    def __str__(self):
        return " Bits: " + '  '.join(map(str, self.bits)) + "\n" + \
            "Bases: " + '  '.join(map(str, self.bases)) + "\n" + \
            "State: " + ' '.join(map(str, self.photons)) + "\n"

    def encode(self):
        return [self._encode(x, y) for x, y in zip(self.bits, self.bases)]

    def _encode(self, bit, basis):
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

def compare_bases(alice_bases, bob_bases):
    return [1 if x == y else 0 for x, y in zip(alice_bases, bob_bases)]


alice = Alice([0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1], list("drdrrrrrddrdddr"))
bob = Bob(list("rddrrddrdrddddr"))
print(alice)
print(bob)
bob.measure(alice.photons, bob.bases)
bob.decode()


print(bob.photons)
print(bob.bits)
print(compare_bases(alice.bases, bob.bases))
