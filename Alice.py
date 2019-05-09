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
            return "→" if basis == 'r' else "↗"
        else:
            return "↑" if basis == 'r' else "↖"
            