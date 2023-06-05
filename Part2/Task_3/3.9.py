from itertools import groupby
lambda s: [(k, sum(1 for _ in g)) for k, g in groupby(s)]
print(rle_encode('ABBCCCDEF'))