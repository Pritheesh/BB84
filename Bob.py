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

    def measure(self, qubits):
        self.measured = True
        self.photons = [self._measure(x, y) for x, y in zip(qubits, self.bases)]

    def _measure(self, state, basis):
        if basis == "r":
            if state in ["→", "↑"]:
                return state
            else:
                return np.random.choice(["→", "↑"])
        else:
            if state in ["↗", "↖"]:
                return state
            else:
                return np.random.choice(["↗", "↖"])

    def decode(self):
        if self.measured:
            self.bits = [1 if x == "↑" or x == "↖"  else 0 for x in self.photons]
        else:
            raise Exception("Not measured to decode.")
        pass


