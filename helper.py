from numpy import random, array, delete

from Alice import Alice
from Bob import Bob

def initialize_alice(length):
    """
    returns Alice object initialized with bits and bases of given length

    Args:
        length - int : length of bits and bases
    Returns: 
        Alice object initialized with given length of bits and bases
    """
    return Alice(random_list(length, "01"), random_list(length, "dr"))

def initialize_bob(length):
    """
    returns Bob object initialized with bases of given length

    Args:
        length - int : length of bases
    Returns: 
        Bob object initialized with given length bases
    """    
    return Bob(random_list(length, "dr"))

def random_list(length, input):
    """
    returns random list of given input with given length
    Args:
        length - int : length of list
        input - string : "01" or "dr"
    Returns: 
        random list of given input with given length
    """
    input = list(input) if input == "dr" else list(map(int, list(input)))
    return random.choice(input, size=length)

def compare_bases(alice_bases, bob_bases):
    """
    Compares the bases of Alice and Bob
    Args:
        alice_bases - list : list of bases 'd' or 'r' of Alice
        bob_bases - list : list of bases 'd' or 'r' of Bob
    Returns: 
        List containing ✓ where match else empty string
    """
    return ["✓" if x == y else '' for x, y in zip(alice_bases, bob_bases)]

def get_match_bits(bits, match_bases):
    """
    Check the key string bits for matched bases
    Args:
        bits - list : list of bits - key string
        match_bases - list : output of compare_bases
    Returns: 
        List containing key bits where bases match - pre-final key
    """
    return [x if y == "✓" else '' for x, y in zip(bits, match_bases)]

def get_discard_bits_indices(block, parity_bits_size, block_size):
    """
    Gives a list of random indices in the key to discard because of exchange in parity bits
    Args:
        block - int : Which chunk
        parity_bits_size - int
        block_size - int
    Returns: 
        List containing indices in the given range 
    """
    start = block * block_size
    return random.choice(range(start, start+block_size), parity_bits_size, replace=False)

def del_list_numpy(key, indices):
    """
    Discards the bits using the indices
    Args:
        key - list : key bits
        indices - list : index positions to delete
    Returns: 
        Remaining list after deleting
    """
    arr = array(key, dtype='int')
    indices = [x for x in indices if x < len(key)]
    return list(delete(arr, indices))
