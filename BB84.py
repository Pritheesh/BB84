import numpy as np
import math
from itertools import zip_longest 
from prettytable import PrettyTable

from hamming import *
from helper import *


KEY_SIZE = 500

BIT_SIZE = 5
n = 2 ** BIT_SIZE - 1
m = BIT_SIZE
k = n - m

h = get_parity_check_matrix(n, m)
g = get_generator_matrix(h)

alice = initialize_alice(KEY_SIZE)
bob = initialize_bob(KEY_SIZE)

alice.encode()

bob.measure(alice.photons)
bob.decode()

compare_list = compare_bases(alice.bases, bob.bases)

prefinal_key = get_match_bits(alice.bits, compare_list)

t = PrettyTable(['']+list(range(KEY_SIZE)))
t.add_row(['Alice bits'] + list(alice.bits))
t.add_row(['Alice bases'] + list(alice.bases))
t.add_row(['Alice photons'] + list(alice.photons))
t.add_row(['Bobs bases'] + list(bob.bases))
t.add_row(['Bobs photons'] + list(bob.photons))
t.add_row(['Equal bits'] + compare_list)
t.add_row(['Bobs Bits'] + list(alice.bits))
t.add_row(['Pre final Key bits'] + prefinal_key)
# print(t)


# print(alice.bits)
prefinal_key = [x for x in prefinal_key if x != ""]
chunks = list(get_chunks(prefinal_key , k))

parity_list = []
for i, chunk in enumerate(chunks):
    chunks[i] = list(chunk)
    encoded = encode(g, chunk, k)
    # print(encoded)
    if np.random.choice([0,1]) == 1:
        random = np.random.randint(4)
        print("Alice introducing error in chunk ", i, "position ", random)
        chunks[i][random] = 1 - chunks[i][random]
    parity_list.append(encoded[-m:])

discard_list = []
for i, (chunk, encoded) in enumerate(zip(chunks, parity_list)):
    encoded = np.concatenate((chunk, encoded))
    decoded = decode(h, encoded)
    n = get_error_from_syndrome(decoded, h)
    if(n != -1 ):
        indices = get_discard_bits_indices(i, m, k)
        discard_list.extend(indices)
        print("Bob Found error in chunk ", i, "position ", n)

print("Length of bits to be removed: ", len(discard_list))
print("Length of key before discard: ", len(prefinal_key))
final_key = del_list_numpy(prefinal_key, discard_list)
print("Length of key after discard: ", len(final_key))
print("Final key: ", final_key)



