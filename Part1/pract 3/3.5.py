#3.5
import random
def fast_mul(a, b):
    s = 0
    while a > 0:
        if a & 1:
            s += b
        a >>= 1
        b <<= 1
    return s
for a in range(100):
    for b in range(100):
        assert fast_mul(a, b) == (a * b)
