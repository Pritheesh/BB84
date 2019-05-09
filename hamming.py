import numpy as np
import math
from itertools import zip_longest 

def get_generator_matrix(h):
    """
    Calculate a generator matrix G, given parity check matrix

    Args:
        h - matrix: a parity check matrix
    Returns: 
        A new generator matrix G
    """
    m, n = h.shape
    return np.concatenate((np.identity(n-m, dtype=int), h[:, :n-m].transpose()), axis=1)


def get_parity_check_matrix(n, m):
    """
    Calculate a parity check matrix of size n x m

    Args:
        n - int : number of message bits in codeword
        m - int : number of parity bits in codeword
    """
    temp = np.zeros((n-m, m), dtype=int)
    index = 0
    for i in range(3, n + 1):
        if not is_power_of_two(i):
            temp[index] = list(str(bin(i)[2:]).zfill(m))
            index += 1
    return np.concatenate((temp.transpose(), np.identity(m, dtype=int)), axis=1)

def is_power_of_two(num):
    """
    Checks if the number is a power of two

    Args:
        num - int 
    """
    return (num & (num - 1)) == 0     

def encode(G, word, k):
    """
    Encode the word using generator matrix G

    Args:
        word - string : data bits to be encoded
        G - matrix : Generator matrix
        k - int: size of data bits
    """
    word = ''.join(map(str,word))
    word = list(map(int, word.zfill(k)))
    return np.dot(word, G) % 2

def decode(H, word):
    """
    Decode the word using Parity Check matrix H

    Args:
        word - string : data bits to be decoded
        H - matrix : Parity Check matrix
    """

    return np.dot(H, word.T) % 2



def get_chunks(iterable, n, padvalue=0):
    return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)


def get_error_from_syndrome(s, h):
    m, n = h.shape
    for i in range(n):
        if np.array_equal(s, h[:, i]):
            return i
    return -1

# h = get_parity_check_matrix(15, 4)
# g = get_generator_matrix(h)

# m = encode(g, str(1010), 11)
# print(h)
# print(m)
# m[2] = 0
# print(decode(h, m))
# transpose = encoded.reshape(-1, 1)
# np.dot(h, transpose)





