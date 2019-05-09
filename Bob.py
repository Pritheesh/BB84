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


