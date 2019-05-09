from functools import reduce

l = [0, 1, 1, 0]
l.reverse()
print(int('0b'+''.join(map(str,l)), 2))
