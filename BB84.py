import numpy as np
from hamming import *
from Alice import Alice
from Bob import Bob

n = 15
k = 11
m = 4

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


# alice = Alice([0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1], list("drdrrrrrddrdddr"))
# bob = Bob(list("rddrrddrdrddddr"))
# print(alice)
# print(bob)

alice = initialize_alice(1024)
bob = initialize_bob(1024)
bob.measure(alice.photons, bob.bases)
bob.decode()


# print(bob.photons)
# print(alice.bits)
# print(bob.bits)
# correct_bits = compare_bases(alice.bases, bob.bases)

h = get_parity_check_matrix(n, m)
g = get_generator_matrix(h)

# print(encode(g, alice.bits[:k], k))
















alice = initialize_alice(22)
# print(alice.bits)
chunks = get_chunks(alice.bits, k)
chunks = list(chunks)
# print(chunks)
encoded_list = []
for i, chunk in enumerate(chunks):
    chunks[i] = list(chunk)
    encoded = encode(g, chunk, k)
    chunks[i][3] = 1 - chunks[i][3]
    encoded_list.append(encoded[-m:])

# print(encoded_list)
# print(chunks)
for chunk, encoded in zip(chunks, encoded_list):
    encoded = np.concatenate((chunk, encoded))
    decoded = decode(h, encoded)
    n = get_error_from_syndrome(decoded, h)
    print(decoded)
    print(n)
print(h)