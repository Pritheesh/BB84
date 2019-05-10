import numpy as np
from hamming import *
from Alice import Alice
from Bob import Bob
from prettytable import PrettyTable

BIT_SIZE = 16
n = 7
k = 4
m = 3

def initialize_alice(length):
    return Alice(generate_random_bits(length), generate_random_bases(length))


def initialize_bob(length):
    return Bob(generate_random_bases(length))


def generate_random_bits(length):
    return np.random.choice([0, 1], size=length)


def generate_random_bases(length):
    return np.random.choice(list("dr"), length)

def compare_bases(alice_bases, bob_bases):
    return ["✓" if x == y else '' for x, y in zip(alice_bases, bob_bases)]

def get_match_bits(alice_bits, match_bits):
    return [x if y == "✓" else '' for x, y in zip(alice_bits, match_bits)]


# alice = Alice([0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1], list("drdrrrrrddrdddr"))
# bob = Bob(list("rddrrddrdrddddr"))
# print(alice)
# print(bob)

alice = initialize_alice(1024)
bob = initialize_bob(1024)




bob.measure(alice.photons)
bob.decode()


# print(bob.photons)
# print(alice.bits)
# print(bob.bits)
# correct_bits = compare_bases(alice.bases, bob.bases)

h = get_parity_check_matrix(n, m)
g = get_generator_matrix(h)

# print(encode(g, alice.bits[:k], k))














t = PrettyTable(['']+list(range(BIT_SIZE)))


alice = initialize_alice(BIT_SIZE)
alice.encode()
t.add_row(['Alice bits'] + list(alice.bits))
t.add_row(['Alice bases'] + list(alice.bases))
t.add_row(['Alice photons'] + list(alice.photons))
bob = initialize_bob(BIT_SIZE)
bob.measure(alice.photons)
bob.decode()
t.add_row(['Bobs bases'] + list(bob.bases))
t.add_row(['Bobs photons'] + list(bob.photons))
t.add_row(['Bobs Bits'] + list(alice.bits))
compare_list = compare_bases(alice.bases, bob.bases)
t.add_row(['Equal bits'] + compare_list)
prefinal_key = get_match_bits(alice.bits, compare_list)
t.add_row(['Pre final Key bits'] + prefinal_key)
print(t)

# print(alice.bits)
prefinal_key = [x for x in prefinal_key if x != ""]
# print(prefinal_key)
chunks = get_chunks(prefinal_key , k)
chunks = list(chunks)
# print(chunks)
encoded_list = []
for i, chunk in enumerate(chunks):
    chunks[i] = list(chunk)
    encoded = encode(g, chunk, k)
    # print(encoded)
    if np.random.choice([0,1]) == 1:
        random = np.random.randint(4)
        print("Alice introducing error in chunk ", i, "position ", random)
        chunks[i][random] = 1 - chunks[i][random]
    encoded_list.append(encoded[-m:])

# print(encoded_list)
# print(chunks)
for i, (chunk, encoded) in enumerate(zip(chunks, encoded_list)):
    encoded = np.concatenate((chunk, encoded))
    decoded = decode(h, encoded)
    n = get_error_from_syndrome(decoded, h)
    if(n != -1 ):
        print("Bob Found error in chunk ", i, "position ", n)
    # print(decoded)
    # print(n)
# print(h)